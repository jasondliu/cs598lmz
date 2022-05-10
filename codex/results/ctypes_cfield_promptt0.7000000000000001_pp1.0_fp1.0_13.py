import ctypes
# Test ctypes.CField

# Create a type with a CField member
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.CField)]

a = A()

# Check access by index
a[0] = "foo"
a[1] = "bar"
assert a[0] == "foo"
assert a[1] == "bar"

# Check access by name
a.a = "foo"
a.b = "bar"
assert a.a == "foo"
assert a.b == "bar"

# Check type
assert type(a[0]) is str
assert type(a[1]) is str
assert type(a.a) is str
assert type(a.b) is str

# Check repr
assert repr(a[0]) == repr("foo")
assert repr(a[1]) == repr("bar")
assert repr(a.a) == repr("foo")
assert repr(a.b) == repr("bar")

# Check equality
assert a[0]
