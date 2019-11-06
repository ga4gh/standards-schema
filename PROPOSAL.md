# GA4GH Standards Schema and API Proposal

## Preamble

The [Genomic Data Toolkit](https://www.ga4gh.org/genomic-data-toolkit/) is a foundational GA4GH resource, allowing individuals to browse our standards. Currently, the toolkit is only human-readable, which has several drawbacks:

1. It is only accessible via web browser. There is no centralized resource for **machine-readable GA4GH standards documentation**, which makes it difficult to develop tooling that works across all GA4GH standards as a whole.

2. There is no search functionality or interactivity, users must manually comb through all standards to find the ones that apply to them.

This approach may be sufficient if the only goal is to disseminate knowledge of our standards to humans. However, we are increasingly seeing use cases that require programs to be aware of multiple standards (e.g. Interoperability Testbed, SchemaBlocks, Network Registries). To maximize the usefulness of these multi-standard, multi-workstream initiatives, there exists a need to have a **structured way of talking about our standards.**

## GA4GH Standards Schema

As the number of new standards and versions released by the GA4GH increases, we'll need a scalable, consistent way of representing all this information so that it can be used in a variety of contexts. For example, each service in a network can refer back to the standard that it's implementing (specification name and version), allowing greater modularity when multiple services in the network employ different versions of the same standard.

To start, I propose a set of schemas that will be able to describe all of our standards. The Standards Schema will act as a data model, and will capture information including, but not limited to:

* Name
* Type/Category (API, File Format, Schema, Policy)
* Descriptions
* Versions/Release history, including changelogs between versions
* Links to where the specification is defined (e.g. the OpenAPI spec)

## GA4GH Standards API

The defined **schemas** can live in SchemaBlocks. However, we will also want to maintain a web-accessible, searchable, up-to-date list of currently released standards. This will require writing JSON documents describing each of our standards, and serving them via a web service/REST API.

The API will provide applications with a means to interface with our standards. It can function as the backend to a searchable web portal (similar to the Genomic Data Toolkit, but with more functionality). In the aforementioned service registry example, each service can use the API to reference the standard version they support. The Standards API would serve multiple other use cases, including aggregating schemas, serving as a foundation for keeping track of implementation registries, and testing implementations for compliance.

The Standards Schema and API can be thought of as a machine-readable source of truth for our standards, making it possible to develop a variety of tools that directly reference specific standards, versions, and documents.

## Example Uses

This section provides examples of use cases, in which a Standards API would help facilitate.

### Versioning Provenance

The underlying data store of a Standards API could serve as the source of truth for released GA4GH products in an application-based context. This would make it possible for services to concretely reference the standard and version they are running.

### "Cave Entrances" for our Standards 

Currently, there is no universal approach to the structuring of our human-readable standards documents. This has led to some standards documents jumping too quickly into technical implementation details without first discussing the standard at a high level, reasons for implementing/use cases, design principles, helpful links, etc. An example of this is [refget](https://samtools.github.io/hts-specs/refget.html), as the link on the Genomic Data Toolkit leads directly to API developer documentation.

Refget and other standards would benefit from a GA4GH documentation build system, which could automatically generate HTML documents from JSON objects stored in the standards API. This would make it possible to:

1. Have consistent visuals/themes across our standards documents
2. Integrate custom subsections, figures, images, etc into each document, as the specific needs for each standard is slightly different
3. Automatically build documentation on a schedule for many standards and versions at once, which will reduce the need for manual maintenance

Again, the Standards API would serve as the hub/data layer for documentation builds. The build system would traverse the API, building docs for the various standards and versions as necessary.

### Modulating Networks of Multiple Service Type and Version

The Service Info and Service Registry standards are used to define federated service networks, in which a single request is passed to multiple servers. An example of this is the Beacon Network. As new versions of standards get released (e.g. Beacon API 2.0), the Beacon Network may end up simultaneously pointing to some Beacons that support the new version, and some that support the old version. This would mean that functions outlined in the new specification are not supported by all Beacons in the network.

To prevent v2.0-type requests from being passed to v1.0 servers, the Standards API could assist in modulating what requests are passed to which Beacon Nodes via the information returned from the Service Info endpoint. For example, if a Beacon's `/service-info` endpoint indicates the service supports `Beacon API v1.0`, we could then use the Standards API to get the OpenAPI Specification for `Beacon API v1.0`. The v1.0 OAI spec does not include the new endpoint, meaning that requests of this type should not be passed to that node from the network master.

This would also support networks of different services (for example, a network with multiple htsget and RNAget servers). If a request of `/reads/{id}` came to the master, then it would be able to cross-reference what is returned by each server's `service-info` endpoint with the OAI spec returned by the Standards API. The resulting information would inform the master to only pass the request to `htsget v1.2.0` servers.

### Decider for Testbed Test Suites 

The Cloud Testbed is a service that will allow implementers to orchestrate various software tests (compliance, integration, etc) on GA4GH-compliant services. Test plugins are configured to run test suites on specific services.

Specific test plugins may become tightly coupled with specific standards, as the API spec that a service is running will say a lot about the tests it can be expected to pass. Thus, certain plugins may be reusable: there may be a default test suite for DRS, or TRS, etc (as there are already standardized tests for refget and RNAget).  

With the Standards API, it will be possible to associate a standard with a test plugin. In a previous example, an implementation's `/service-info` endpoint could give us the matching standard and version definition from the Standards API. Then, if the standard references a specific test plugin, we can set the implementation to run the test suite without manual configuration.

The Standards API forms a bridge between an implementation's `/service-info`, and the test suite the orchestrator will run:

Service Info <-> Standards API <-> Testbed Orchestrator

As an example:

* The testbed orchestrator is aware of multiple services in its registry, one of them being `https://example-htsget.org`
* `GET https://example-htsget.org/service-info` tells us that the implementation is an "htsget v1.2.0" server
* The testbed orchestrator can get the test plugin document for "htsget v1.2.0" via `GET https://ga4gh-standards.org/standards/htsget/v1.2.0/plugin`
* The testbed orchestrator runs those tests automatically, without having to write a new plugin, or having to manually import it

In this context, the Standards API would contribute to test plugin reusability, as the same plugins can be employed across different registries/networks.

## Summary

In short, a Standards Schema and API would:

* Provide a consistent, structured, machine-readable format for describing and cataloguing the products of GA4GH, namely, our standards.
* Provide a structured language for describing the **connections** between standards (e.g. for a particular implementation, *id* refers to the same sample in RNAget and htsget).
* Provide a centralized resource for learning about our standards, so that newcomers and external users don't have to manually search for each standard across multiple Github organizations, repositories, and subdirectories.
* Serve as the underlying backend to a standards portal web interface, similar to the ISO [Online Browsing Platform](https://www.iso.org/obp/ui/).
* Enable the development of pan-GA4GH (cross workstream) tooling, such as automated swagger client generation or automated documentation generation, which would help shorten development times and enable a more cohesive documentation base.
* For schema-based standards (e.g. PhenoPackets, VR, SchemaBlocks), an overarching Standards API could essentially integrate all schemas, making it easier to work with object classes across multiple schemas.
* Allow researchers and developers to easily locate GA4GH-backed implementations
* Serve as a foundation for implementation registries, allowing GA4GH to maintain awareness of implementation networks.
* Allow our registries to integrate with the Cloud Testbed (I foresee the Testbed becoming a pan-GA4GH solution). With our Standards API rigged to the Testbed, we can monitor (on an automated schedule) the status of implementations in our registries. This will allow us to automatically remove implementations that do not conform with the specification from our registry.
