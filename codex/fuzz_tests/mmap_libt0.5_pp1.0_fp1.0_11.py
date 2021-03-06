import mmap
from ctypes import *
from ctypes.wintypes import *


# Constants

# Constants for GetVersionExW
VER_NT_WORKSTATION = 0x0000001
VER_NT_DOMAIN_CONTROLLER = 0x0000002
VER_NT_SERVER = 0x0000003
VER_SUITE_SMALLBUSINESS = 0x00000001
VER_SUITE_ENTERPRISE = 0x00000002
VER_SUITE_TERMINAL = 0x00000010
VER_SUITE_DATACENTER = 0x00000080
VER_SUITE_SINGLEUSERTS = 0x00000100
VER_SUITE_PERSONAL = 0x00000200
VER_SUITE_BLADE = 0x00000400
VER_SUITE_EMBEDDEDNT = 0x00000800
VER_SUITE_STORAGE_SERVER = 0x00002000
VER_SUITE_COMPUTE_SERVER = 0x00004000
VER_SUITE_WH_SERVER = 0x00008000

# Constants for GetSystemInfo
PROC
