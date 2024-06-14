from vault.abc import VaultABC
from vault.linux.secret_tool import clear_password, lookup_password, store_password


class LinuxVault(VaultABC):
    def add_secret(self, name, secret):
        return store_password(name, secret)

    def get_secret(self, name):
        return lookup_password(name)

    def remove_secret(self, name):
        return clear_password(name)