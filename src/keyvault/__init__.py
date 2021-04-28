from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient as AzSecretClient, KeyVaultSecret
from os import getenv
from dotenv import load_dotenv


class SecretClient:
    def __init__(self, vault_name: str) -> None:
        vault_url = f'https://{vault_name}.vault.azure.net'
        credential = DefaultAzureCredential()
        self.client = AzSecretClient(vault_url=vault_url, credential=credential)

    def get_secret(self, secret_name: str, secret_version: str = "") -> KeyVaultSecret:
        load_dotenv()
        self._check_env_variables()
        return self.client.get_secret(name=secret_name, version=secret_version)

    @staticmethod
    def _check_env_variables() -> bool:
        if not getenv('AZURE_CLIENT_ID') or not getenv('AZURE_CLIENT_SECRET') or not getenv('AZURE_TENANT_ID'):
            raise ValueError(''' you should set needed env variables:
                - AZURE_CLIENT_ID
                - AZURE_CLIENT_SECRET
                - AZURE_TENANT_ID
            ''')
        return True
