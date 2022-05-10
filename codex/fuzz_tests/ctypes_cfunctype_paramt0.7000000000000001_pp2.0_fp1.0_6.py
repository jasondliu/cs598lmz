import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

class Struct:
    def __init__(self, *fields):
        self.fields = fields
        self.__dict__.update(zip(fields, [None] * len(fields)))

class Interface:
    def __init__(self, name, methods):
        self.name = name
        self.methods = methods

class Method:
    def __init__(self, name, in_types, out_types, flags):
        self.name = name
        self.flags = flags
        self.in_types = in_types
        self.out_types = out_types

class Option:
    def __init__(self, name, interface, flags):
        self.name = name
        self.interface = interface
        self.flags = flags

class Object:
    def __init__(self, ptr, interface=None):
        self.ptr = ptr
        self.interface = interface

    def __getattr__(self, name):
        return self.interface.methods[name]

    def __setattr__(
