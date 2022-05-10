from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = 8
s.__init__(s.format)
s.pack(1, 2, 3)

# Issue #17863: test the struct.__new__ implementation.
Struct.__new__(Struct, 'ii')

# Issue #17864: test that Struct.__new__ doesn't accept too many args.
try:
    Struct.__new__(Struct, 'ii', 'extra')
except TypeError:
    pass
else:
    raise Exception

# Issue #17864: test that Struct.__new__ doesn't accept too few args.
try:
    Struct.__new__(Struct)
except TypeError:
    pass
else:
    raise Exception

# Issue #17865: test that Struct.__new__ rejects bad formats.
try:
    Struct.__new__(Struct, 'z')
except TypeError:
    pass
else:
    raise Exception

# Issue #17865: test that Struct.__new__ rejects bad formats.
