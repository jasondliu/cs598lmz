import ctypes
# Test ctypes.CField
#
# From http://docs.python.org/lib/ctypes-fields.html
#
# ctypes.CField(type, offset[, bitsize])
#
# This is a class factory that returns a new class with a field definition
# for a C field. The class is derived from ctypes.Structure, and has a
# single field, named name, defined for it.
#
# type is the ctypes type of the field. offset is the offset of the field
# in bytes, relative to the beginning of the structure. bitsize is the size
# of the field in bits, and defaults to the size of type.
#
# The new class has a class attribute _pack_ = 1, this is needed to tell
# ctypes to pack the structure.
#

#
# From http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_data_types.asp
#
# typedef struct _SYSTEMTIME {
#   WORD wYear;
#   WORD wMonth;
#   WORD w
