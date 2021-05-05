# Azure Integration

this package is an azure integration to use in the DTRG team.

for now, we just have vault integration in the package.

# HOW TO USE
### - From pypi
first, you need to install the package. to do so create a personal access token and then connect to the feed [according to these instructions.](https://dev.azure.com/keyleadhealth/Klinik/_packaging?_a=connect&feed=azure-integration) (choose pip)

then install the package:
```shell
$ pip install azure-integration # this will install latest version.
```

you need to set these env variables to access to azure:
```shell
AZURE_CLIENT_ID=YOUR_CLIENT_ID
AZURE_CLIENT_SECRET=YOUR_CLIENT_SECRET
AZURE_TENANT_ID=YOUR_TENANT_ID
```

### Secret Client
to use secret client you can do something like this:
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

### Service Name Finder
__this utility is implemented to use in dtrg projects.__

this utility will help you find needed credentials such as key vault name, postgres server address and postgres admin password secret name.
remember in development environment you should set WEBSITE_SITE_NAME to a valid website name according to patterns we use in dtrg project.

you can use it simply:
```python
from dtrg_specified import ServiceNameFinder

service_name_finder = ServiceNameFinder()
service_name_finder.kv_name # will return key vault name
service_name_finder.psql_host # will return postgres host host
service_name_finder.psql_password_secret_name # will return postgres password secret name

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
