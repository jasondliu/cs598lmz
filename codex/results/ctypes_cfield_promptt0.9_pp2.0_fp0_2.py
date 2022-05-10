import ctypes
# Test ctypes.CField
assert ctypes.CField.__doc__ == None
assert CField.__doc__ == None
assert CField.__name__ == 'CField'

class X(ctypes._SimpleCData):
    _type_ = "L"
    _check_retval_ = lambda x: False

class Y(ctypes._SimpleCData):
    _type_ = "P"
    _check_retval_ = lambda x: False

class Z(ctypes._SimpleCData):
    _type_ = "L"
    _check_retval_ = lambda x: False

class Struct(ctypes.Structure):
    _fields_ = [
        ('a', X),
        ('b', Y),
        ('c', X),
        ('d', Y),
        ('e', Z),
        ]

assert [x for x in Struct._anonymous_] == [
    ('_0', Y),
    ('_1', Y)
    ]

assert [x for x in Struct._fields_] == [
    ('a', X),
    ('b',
