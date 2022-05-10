import ctypes
# Test ctypes.CField.
#
# This test was provided by Thomas Heller.
#
# To run this test, the Python interpreter must be compiled with the
# following preprocessor macros defined:
#
#   Py_TRACE_REFS
#   WITH_CYCLE_GC
#
# This is the case for debug builds of Python.
import ctypes
from ctypes import *

LONG = c_long
ULONG_PTR = POINTER(c_ulong)
class VOLUME(Structure):
    pass
VOLUME._fields_ = [
    ('SerialNumber', ULONG_PTR),
    ('NumberOfSectors', ULONG_PTR),
    ('TotalClusters', ULONG_PTR),
    ('FreeClusters', ULONG_PTR),
    ('SectorsPerCluster', ULONG_PTR),
    ('BytesPerSector', ULONG_PTR),
]

class VOLINFO(Structure):
    _fields_ = [
        ('ulVolSer', c_ulong),
        ('cch', c_ulong),
        ('szVol
