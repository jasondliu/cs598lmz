import _structures
from _structures import *
from _structures import _fields_

# =============================================================================
#
# =============================================================================

class _HANDLE(Structure):
    pass

PVOID = c_void_p
HANDLE = PVOID

# =============================================================================
#
# =============================================================================

class _UNICODE_STRING(Structure):
    _fields_ = [
        ('Length',        USHORT),
        ('MaximumLength', USHORT),
        ('Buffer',        PWSTR),
    ]

UNICODE_STRING = _UNICODE_STRING

# =============================================================================
#
# =============================================================================

class _OBJECT_ATTRIBUTES(Structure):
    _fields_ = [
        ('Length',                   ULONG),
        ('RootDirectory',            HANDLE),
        ('ObjectName',               POINTER(UNICODE_STRING)),
        ('Attributes',               ULONG),
        ('SecurityDescriptor',       PVOID),
        ('SecurityQualityOfService', PVOID),
    ]

OBJECT_AT
