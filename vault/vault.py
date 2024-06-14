from logging import getLogger
import platform
from vault.abc import VaultABC
from vault.linux.vault import LinuxVault
from vault.macos.vault import MacOSVault
from vault.windows.vault import WindowsVault


logger = getLogger()

Vault:VaultABC = None

system_platform = platform.system()
if system_platform == 'Windows':
    Vault = WindowsVault()
elif system_platform == 'Darwin':
    Vault = MacOSVault()
elif system_platform == 'Linux':
    Vault = LinuxVault()
else:
    logger.info(f'Platform {system_platform} is not supported')