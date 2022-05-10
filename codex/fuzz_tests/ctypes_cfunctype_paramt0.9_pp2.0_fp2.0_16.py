import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

class Field:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Field: {!r}>'.format(self.name)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, val):
        setattr(instance, self.name, val)

class StructMeta(type):
    pass

class BaseStruct(metaclass=StructMeta):
    @classmethod
    def from_address(cls, addr):
        inst = cls()
        ctypes.memmove(inst, ctypes.c_voidp(addr), ctypes.sizeof(inst))
        return inst

    def as_address(self):
        return ctypes.addressof(self)

    def to_bytes(self):
        return bytearray(self)

    def __len__(self):
        return ctypes
