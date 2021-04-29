# Azure Integration

this package is an azure integration to use in the DTRG team.

for now, we just have vault integration in the package.

# HOW TO USE
first, you need to install the package. to do so create a personal access token and then connect to the feed [according to these instructions.](https://dev.azure.com/keyleadhealth/Klinik/_packaging?_a=connect&feed=azure-integration) (choose pip)

then install the package:
```shell
$ pip install azure-integration==0.0.2
```

also, there's another way to get the package from azure artifacts:
```shell
$ az artifacts universal download \
  --organization "https://dev.azure.com/keyleadhealth/" \
  --project "da4824a3-d087-4024-a144-a3d3265a9d6e" \
  --scope project \
  --feed "azure-integration" \
  --name "azure-integration" \
  --version "0.0.2" \
  --path .
```

then install the package using pip through your environment:
```shell
$ pip install azure_integration-0.0.1-py3-none-any.whl
```

you need to set these env variables to access to azure:
```shell
AZURE_CLIENT_ID=YOUR_CLIENT_ID
AZURE_CLIENT_SECRET=YOUR_CLIENT_SECRET
AZURE_TENANT_ID=YOUR_TENANT_ID
```

then you can use it like this:
```python
from keyvault import SecretClient

client = SecretClient(VAULT_NAME)
client.get_secret(SECRET_NAME)  # this returns KeyVaultSecret object
client.get_secret(SECRET_NAME).value  # this returns secret value as string
```

also, you can get a dict of secrets wherever you need, ex setting.py:
```python
from keyvault import SecretClient

[... whatever settings ...]

client = SecretClient(VAULT_NAME)
needed_secrets = {
    "SECRET_NAME": "SECRET_VERSION", # you can leave version blank
    "SECOND_SECRET_NAME": "SECOND_SECRET_VERSION"
}
c.get_secrets(needed_secrets)  # this will return results as KeyVaultSecret
c.get_secrets_values(needed_secrets)  # this will return results as str
```
note that you don't need to assign `get_secrets` and `get_secrets_values` functions' return value and that's because it will modify the given dict object and you can access the values within it.

# HOW TO BUILD
if you want to build the module yourself follow the steps:
- clone this repository.
- create a venv inside it.
- install requirements by running:
```shell
$ pip install -r requirements.txt
```
- then build it:
```shell
$ python -m build
```
