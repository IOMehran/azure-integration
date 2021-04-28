# Azure Integration

this package is an azure integration to use in DTRG team.

for now, we just have vault integration in the package.

# HOW TO USE
first, get the package from azure artifacts:
```shell
$ az artifacts universal download \
  --organization "https://dev.azure.com/keyleadhealth/" \
  --project "da4824a3-d087-4024-a144-a3d3265a9d6e" \
  --scope project \
  --feed "azure-integration" \
  --name "azure-integration" \
  --version "0.0.1" \
  --path .
```

then install the package thorough your environment:
```shell
$ pip install azure_integration-0.0.1-py3-none-any.whl
```

you need to set these env variables in order to access to azure:
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
