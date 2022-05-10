import _struct
import ctypes

#
# Constants
#

# The following constants define the type of the transaction.
#
# Note:  The constants are defined here for use in the user mode.
#        The kernel mode should use fltKernel.h constants.

FLT_PARAM_OPERATION_NAME = 0x00000001
FLT_PARAM_TRANSACTION_CONTEXT = 0x00000002
FLT_PARAM_TRANSACTION_STATUS = 0x00000004

#
# Structures
#

class FLT_TRANSACTION_CONTEXT(ctypes.Structure):
    _fields_ = [
        ('Flags', ULONG),
        ('Reserved1', ULONG),
        ('Reserved2', ULONG),
        ('Reserved3', ULONG),
    ]

