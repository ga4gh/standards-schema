# StandardVersion Schema

```
http://schemas.ga4gh.org:8000/schemas/standardversion
```

a description

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                                 |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ---------------------------------------------------------- |
| Can be instantiated | No         | Experimental | No           | Forbidden         | Permitted             | [standardversion.schema.json](standardversion.schema.json) |

# StandardVersion Properties

| Property              | Type     | Required     | Nullable | Defined by                                 |
| --------------------- | -------- | ------------ | -------- | ------------------------------------------ |
| [spec_url](#spec_url) | `string` | **Required** | No       | StandardVersion (this schema)              |
| [version](#version)   | `string` | **Required** | No       | StandardVersion (this schema)              |
| `*`                   | any      | Additional   | Yes      | this schema _allows_ additional properties |

## spec_url

`spec_url`

- is **required**
- type: `string`
- defined in this schema

### spec_url Type

`string`

## version

`version`

- is **required**
- type: `string`
- defined in this schema

### version Type

`string`
