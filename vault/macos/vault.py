from vault.abc import VaultABC
from vault.macos.security import add_generic_password, delete_generic_password, find_generic_password


class MacOSVault(VaultABC):
    def add_secret(self, name, secret):
        return add_generic_password(name, secret)
    
    def get_secret(self, name):
        return find_generic_password(name)
    
    def remove_secret(self, name):
        return delete_generic_password(name)