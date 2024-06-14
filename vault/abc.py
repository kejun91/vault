from abc import ABC, abstractmethod


class VaultABC(ABC):
    @abstractmethod
    def add_secret(self, name, secret):
        pass
    
    @abstractmethod
    def get_secret(self, name):
        pass
    
    @abstractmethod
    def remove_secret(self, name):
        pass