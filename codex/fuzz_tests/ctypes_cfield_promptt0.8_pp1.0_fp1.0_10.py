import ctypes
# Test ctypes.CField.__get__
class Record(ctypes.Structure):
    _fields_ = [("field1", ctypes.c_int),
                ("field2", ctypes.c_int * 3)]

print Record.field1.__get__(None, Record)
print Record.field1.__get__(Record(), Record)
print Record.field2.__get__(None, Record)
print Record.field2.__get__(Record(), Record)

print Record().field1
print Record().field2
