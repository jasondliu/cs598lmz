import ctypes
# Test ctypes.CField.__set__ and CField.__get__
# Overloading CField methods
# We will store and retrieve the value of a secret member field
# from a python class and from a C struct
import _ctypes

class SimpleClass:

    def __setattr__(self, name, value):
        from _ctypes import FunctionType
        if not isinstance(value, FunctionType):
            raise TypeError("Only functions are allowed as members")
        # Make a CField instance
        cfield = ctypes.CField()
        # cfield.offset = first_field_offset.
        # This is only defined in the context of a C struct.
        cfield.offset = _ctypes.offsetof(SomeStruct, "empty")
        # We will use the following ctypes structure
        # instead of the SimpleClass instance
        cfield.__set__(SomeStruct(), value)

class SomeStruct(ctypes.Structure):
    _fields_ = [
        ("empty", ctypes.c_int),
        ("value", ctypes.c_int)
                ]

class AnotherStruct(
