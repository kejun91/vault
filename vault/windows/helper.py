import ctypes
from ctypes.wintypes import DWORD, LPCWSTR, LPWSTR, BOOL, LPBYTE
from ctypes import POINTER, Structure
from logging import getLogger
import platform

logger = getLogger()

if platform.system() == 'Windows':
    from ctypes import windll

class CREDENTIAL_ATTRIBUTE(Structure):
    _fields_ = [
        ("Keyword", LPWSTR),
        ("Flags", DWORD),
        ("ValueSize", DWORD),
        ("Value", LPBYTE)
    ]

class CREDENTIAL(Structure):
    _fields_ = [
        ("Flags", DWORD),
        ("Type", DWORD),
        ("TargetName", LPWSTR),
        ("Comment", LPWSTR),
        ("LastWritten", DWORD),
        ("CredentialBlobSize", DWORD),
        ("CredentialBlob", LPBYTE),
        ("Persist", DWORD),
        ("AttributeCount", DWORD),
        ("Attributes", POINTER(CREDENTIAL_ATTRIBUTE)),
        ("TargetAlias", LPWSTR),
        ("UserName", LPWSTR)
    ]

def get_generic_credential(target_name):
    advapi32 = windll.advapi32
    CredReadW = advapi32.CredReadW
    CredReadW.argtypes = [LPCWSTR, DWORD, DWORD, POINTER(POINTER(CREDENTIAL))]
    CredReadW.restype = BOOL

    # Convert target_name to LPCWSTR
    target_name = LPCWSTR(target_name)

    # Read the credential
    credential = POINTER(CREDENTIAL)()
    if CredReadW(target_name, 1, 0, ctypes.byref(credential)):
        addr = ctypes.addressof(credential.contents.CredentialBlob)
        bts = ctypes.string_at(addr,1000).replace(b'\x00',b'')
        return extract_bytes(bts,b'upwebtoolsstart-',b'-upwebtoolsend').decode('utf-8')
    else:
        logger.error("failed to read credential")
        return None

def extract_bytes(data, start_pattern, end_pattern):
    start_index = data.find(start_pattern)
    if start_index == -1:
        return None  # Start pattern not found

    end_index = data.find(end_pattern, start_index + len(start_pattern))
    if end_index == -1:
        return None  # End pattern not found

    return data[start_index + len(start_pattern):end_index]