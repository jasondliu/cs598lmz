import ctypes
# Test ctypes.CField
class Field(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_long),
        ('y', ctypes.c_long)
        ]
    x = ctypes.c_float
    y = ctypes.c_float

Field._fields_ = [('x', ctypes.c_double),
                  ('y', ctypes.c_double)]

Field._fields_ = [('x', ctypes.c_long),
                  ('y', ctypes.c_long)]
print(type(Field.x))
print(type(Field.x.__get__(None)))
print(type(Field.x.__get__(None, None)))
print(type(Field.x.__get__(None, object)))
print(type(Field.x.__get__(Field(1, 2), None)))
print(type(Field.x.__get__(Field(1, 2), object)))
print(Field.x.offset)
print(Field.y.offset)
# Check that fields can be replaced
f = Field(1
