import _struct
from _struct import calcsize
import _ctypes
from Image import *

# p2e version information
Version_Major = 1
Version_Minor = 0
Version_Release = 0
Version_BuildNumber = 0
Version_SEQNO = 0

FullVersion = '1.0.0.0'
Version = 100
Version_DLL = '1.0.0.0'
# Patch this in from a global variable, we are using p2e devel libs in PyRhino
Revision = P2E_HG_REVISION

# P2E_TYPES (used in structs)
P2ET_INVALID = 0
P2ET_CHAR = 1  # 8-bit integer value
P2ET_UCHAR = 2
P2ET_SHORT = 3
P2ET_USHORT = 4
P2ET_INT = 5
P2ET_UINT = 6
P2ET_LONG = 7  # 32-bit integer value
P2ET_ULONG = 8
P2ET_FLOAT = 9
P2ET_
