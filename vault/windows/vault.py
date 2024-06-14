from vault.abc import VaultABC
from vault.windows.credential_manager import add_generic_credential, delete_generic_credential
from vault.windows.helper import get_generic_credential


class WindowsVault(VaultABC):
    def add_secret(self, name, secret):
        return add_generic_credential(name, secret)
    
    def get_secret(self, name):
        return get_generic_credential(f"UpWebTools/{name}")
    
    def remove_secret(self, name):
        return delete_generic_credential(name)