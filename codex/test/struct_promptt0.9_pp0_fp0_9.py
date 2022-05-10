import _struct
# Test _struct.Struct.
#
# Check _struct.Struct("i")('\0\0\0\0') raises an error.
# Check _struct.Struct("i")("") raises an error.
import _struct
# This used to crash the Python interpreter.
# The compiler now uses PyNode_FREE instead of PyNode_DecRef.
