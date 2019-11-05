# GA4GH Standards Schema and API Proposal

## Preamble

The [Genomic Data Toolkit](https://www.ga4gh.org/genomic-data-toolkit/) is a foundational GA4GH resource, allowing individuals to browse our standards. Currently, the toolkit is only human-readable, which has several drawbacks:

1. It is only accessible via web browser. There is no centralized resource for **machine-readable GA4GH standards documentation**, which makes it difficult to develop tooling that works across all GA4GH standards as a whole.

2. There is no search functionality or interactivity, users must manually comb through all standards to find the ones that apply to them.

This approach may be sufficient if the only goal is to disseminate knowledge of our standards to humans. However, we are increasingly seeing use cases that require programs to be aware of multiple standards (e.g. Interoperability Testbed, SchemaBlocks, Network Registries). To maximize the usefulness of these multi-standard, multi-workstream initiatives, there exists a need to have a **structured way of talking about our standards.**

## GA4GH Standards Schema

As the number of new standards and versions released by the GA4GH increases, we'll need a scalable, consistent way of representing all this information so that it can be used in a variety of contexts. For example, each service in a network can refer back to the standard that it's implementing (specification name and version), allowing greater modularity when multiple services in the network employ different versions of the same standard.

To start, I propose a set of schemas that will be able to describe all of our standards. The Standards schema will capture information including, but not limited to:

* Name
* Type/Category (API, File Format, Schema, Policy)
* Descriptions
* Versions/Release history, including changelogs between versions
* Links to where the specification is defined (e.g. the OpenAPI spec)

## GA4GH Standards API

The defined **schemas** can live in SchemaBlocks. However, we will also want to maintain a web-accessible, searchable, up-to-date list of **instances** of currently released standards. This will require writing JSON documents describing each of our standards, and serving them via a web service/REST API.

The API will provide applications with a means to interface with our standards. It can function as the backend to a searchable web portal (similar to the Genomic Data Toolkit, but with more functionality). In the aforementioned service registry example, each service can use the API to reference the standard version they support. The Standards API would serve multiple other use cases, including aggregating schemas, serving as a foundation for keeping track of implementation registries, and testing implementations for compliance.

The Standards Schema and API can be thought of as a machine-readable source of truth for our standards, making it possible to develop a variety of tools that directly reference specific standards, versions, and documents.

## Summary

In short, a Standards Schema and API would:

* Provide a consistent, structured, machine-readable format for describing and cataloguing the products of GA4GH, namely, our standards.
* Provide a structured language for describing the **connections** between standards (e.g. for a particular implementation, *id* refers to the same sample in RNAget and htsget).
* Provide a centralized resource for learning about our standards, so that newcomers and external users don't have to manually search for each standard across multiple Github organizations, repositories, and subdirectories.
* Serve as the underlying backend to a standards portal web interface, similar to the ISO [Online Browsing Platform](https://www.iso.org/obp/ui/).
* Enable the development of pan-GA4GH (cross workstream) tooling, such as automated swagger client generation or automated documentation generation, which would help shorten development times and enable a more cohesive documentation base
* For schema-based standards (e.g. PhenoPackets, VR, SchemaBlocks), an overarching Standards API could essentially integrate all schemas, making it easier to work with object classes across multiple schemas
* Allow researchers and developers to easily locate GA4GH-backed implementations
* Serve as a foundation for implementation registries, allowing GA4GH to maintain awareness of implementation networks
* Allow our registries to integrate with the Cloud Testbed (I foresee the Testbed becoming a pan-GA4GH solution). With our Standards API rigged to the Testbed, we can monitor (on an automated schedule) the status of implementations in our registries. This will allow us to automatically remove implementations that do not conform with the specification from our registry.
