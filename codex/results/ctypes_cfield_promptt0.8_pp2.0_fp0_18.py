import ctypes
# Test ctypes.CField.

import ctypes
class Field:
    def __init__(self, type, name=None):
        self.type = type
        self.name = name
        self.field = None
    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.field is None:
            self.field = ctypes.CField(self.type, self.name)
        return self.field.get(obj)
    def __set__(self, obj, value):
        if self.field is None:
            self.field = ctypes.CField(self.type, self.name)
        self.field.set(obj, value)

class C(ctypes.Structure):
    _fields_ = [
        ("x", "c"),
        ("y", "c"),
        ("i", "h"),
        ("j", "h"),
        ("f", "h"),
        ("g", "h"),
        ("ascii", "c"),
        ("ascii0", "c"),
        ("us
