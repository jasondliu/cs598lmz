import ctypes
# Test ctypes.CField
assert l.CField.a == l.CField().a
assert l.CField.b == l.CField().b
assert l.CField.c == l.CField().c
# Test ctypes.CStruct
assert l.CStruct.x == l.CStruct().x
assert l.CStruct.y == l.CStruct().y
# Test ctypes.CPrimitive
assert l.CPrimitive.a == l.CPrimitive().a
assert l.CPrimitive.b == l.CPrimitive().b
assert l.CPrimitive.c == l.CPrimitive().c
assert l.CPrimitive.s == l.CPrimitive().s
assert l.CPrimitive.e == l.CPrimitive().e
# Test ctypes.CUnion
assert l.CUnion.x == l.CUnion().x
assert l.CUnion.y == l.CUnion().y
# Test custom ctypes.Structure
class SubclassCField(l.CField):
    _fields_ = [("third", ctypes.c_double)]

assert
