from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f', True)
s.size
s.pack(1, 0, 2.7)
s.unpack(_)
s.unpack_from(bytes(s.size), 0)
s.unpack_from(bytes(s.size + 1), 1)
s.unpack_from(memoryview(bytes(s.size + 1)), 1)

# Issue #23609: segfault when packing a tuple with a single bool
try:
    Struct(b'?').pack((True,))
except TypeError as e:
    assert e.args[0] == 'pack requires a bytes object of length 1'

# Issue #23609: segfault when packing a tuple with a single bool
try:
    Struct(b'?').pack((False,))
except TypeError as e:
    assert e.args[0] == 'pack requires a bytes object of length 1'

# Issue #23609: segfault when packing a tuple with a single bool
try:
    Struct(b'?').pack((1,))

