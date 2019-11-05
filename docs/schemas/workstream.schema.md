# WorkStream Schema

```
http://schemas.ga4gh.org:8000/schemas/workstream
```

a description

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                       |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ------------------------------------------------ |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [workstream.schema.json](workstream.schema.json) |

# WorkStream Properties

| Property      | Type   | Required     | Nullable | Defined by                                 |
| ------------- | ------ | ------------ | -------- | ------------------------------------------ |
| [name](#name) | `enum` | **Required** | No       | WorkStream (this schema)                   |
| `*`           | any    | Additional   | Yes      | this schema _allows_ additional properties |

## name

a thing

`name`

- is **required**
- type: `enum`
- defined in this schema

The value of this property **must** be equal to one of the [known values below](#name-known-values).

### name Known Values

| Value       | Description |
| ----------- | ----------- |
| `ClinPheno` |             |
| `Cloud`     |             |
| `Discovery` |             |
| `DURI`      |             |
| `LSG`       |             |
| `GKS`       |             |
