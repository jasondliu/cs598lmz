import mmap
# Test mmap.mmap memory-mapped file read-only mode (e.g., acc.exe.core) automatically
from mmap import ACCESS_READ, ALLOCATIONGRANULARITY
from os import strerror
from os.path import getsize
from platform import architecture


ARCHITECTURE = architecture()[0]


#
# Global type definitions
#

NONC_WILDCARD 		= -1

KID_WILDCARD 		= -1
SID_WILDCARD 		= -1	# state index

KID_INIT 			= -2
KID_END 			= -3

RTYPE_WILDCARD 		= -1
RTYPE_HINT_WILDCARD = -2

ITYPE_WILDCARD		= 0x0
STYPE_WILDCARD 		= 0x0

# For aikid operations and flags.
AOP_TRACE_START		= 1
AOP_TRACE_START_HALT = 2
A
