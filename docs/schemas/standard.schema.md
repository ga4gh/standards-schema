# Standard Schema

```
http://schemas.ga4gh.org:8000/schemas/standard
```

a description

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                   |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | -------------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [standard.schema.json](standard.schema.json) |

## Schema Hierarchy

- Standard `http://schemas.ga4gh.org:8000/schemas/standard`
  - [WorkStream](workstream.schema.md) `http://schemas.ga4gh.org:8000/schemas/workstream`

# Standard Properties

| Property                                          | Type            | Required     | Nullable | Defined by                                 |
| ------------------------------------------------- | --------------- | ------------ | -------- | ------------------------------------------ |
| [additional_workstreams](#additional_workstreams) | WorkStream      | Optional     | No       | Standard (this schema)                     |
| [category](#category)                             | `enum`          | Optional     | No       | Standard (this schema)                     |
| [long_description](#long_description)             | `string`        | **Required** | No       | Standard (this schema)                     |
| [name](#name)                                     | `string`        | **Required** | No       | Standard (this schema)                     |
| [primary_workstream](#primary_workstream)         | WorkStream      | **Required** | No       | Standard (this schema)                     |
| [short_description](#short_description)           | `string`        | **Required** | No       | Standard (this schema)                     |
| [versions](#versions)                             | StandardVersion | **Required** | No       | Standard (this schema)                     |
| `*`                                               | any             | Additional   | Yes      | this schema _allows_ additional properties |

## additional_workstreams

`additional_workstreams`

- is optional
- type: WorkStream
- defined in this schema

### additional_workstreams Type

Array type: WorkStream

All items must be of the type:

- [WorkStream](workstream.schema.md) – `http://schemas.ga4gh.org:8000/schemas/workstream`

## category

`category`

- is optional
- type: `enum`
- defined in this schema

The value of this property **must** be equal to one of the [known values below](#category-known-values).

### category Known Values

| Value        | Description |
| ------------ | ----------- |
| `API`        |             |
| `FileFormat` |             |
| `Schema`     |             |
| `Policy`     |             |

## long_description

`long_description`

- is **required**
- type: `string`
- defined in this schema

### long_description Type

`string`

## name

`name`

- is **required**
- type: `string`
- defined in this schema

### name Type

`string`

## primary_workstream

`primary_workstream`

- is **required**
- type: WorkStream
- defined in this schema

### primary_workstream Type

- [WorkStream](workstream.schema.md) – `http://schemas.ga4gh.org:8000/schemas/workstream`

## short_description

`short_description`

- is **required**
- type: `string`
- defined in this schema

### short_description Type

`string`

## versions

`versions`

- is **required**
- type: StandardVersion
- defined in this schema

### versions Type

Array type: StandardVersion

All items must be of the type:

- [StandardVersion](standardversion.schema.md) – `http://schemas.ga4gh.org:8000/schemas/standardversion`
