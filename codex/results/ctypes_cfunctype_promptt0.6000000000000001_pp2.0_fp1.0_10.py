import ctypes
# Test ctypes.CFUNCTYPE()
from ctypes import *

def _check_type(typ):
    if isinstance(typ, type):
        typ = typ.__ctype_be__
    if isinstance(typ, ctypes._SimpleCData):
        return True
    if isinstance(typ, ctypes.Array):
        return _check_type(typ._type_)
    if isinstance(typ, ctypes.Structure):
        for field_name, field_type in typ._fields_:
            if not _check_type(field_type):
                return False
        return True
    if isinstance(typ, ctypes.Union):
        for field_name, field_type in typ._fields_:
            if not _check_type(field_type):
                return False
        return True
    if isinstance(typ, ctypes.Pointer):
        return _check_type(typ._type_)
    if isinstance(typ, ctypes.CFUNCTYPE):
        for arg_type in typ.argtypes:
            if not _check_type(arg_type):

