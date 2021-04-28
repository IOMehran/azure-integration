from dotenv import load_dotenv
from src.keyvault import SecretClient

import os
import unittest


class TestSecretClient(unittest.TestCase):
    load_dotenv()
    c = SecretClient(os.getenv('AZURE_KV_NAME'))

    def test_get_secret(self):
        secret = self.c.get_secret('test')
        self.assertTrue(secret)
        self.assertTrue(type(secret.value) == str)
