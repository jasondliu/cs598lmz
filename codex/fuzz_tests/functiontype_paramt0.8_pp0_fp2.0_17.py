from types import FunctionType
list(FunctionType(x).keywords) == [('x', 1), ('y', 2)]

# str and bytes conversions
assert list(str(x)) == list(x)
b = bytes(x)
assert list(b) == [b'a', b'b', b'c']
assert b[0] == b'a'
c = bytearray(x)
assert list(c) == [b'a', b'b', b'c']
assert c[0] == b'a'
assert bytes(b) == b
assert bytes(c) == b

# memoryview, buffer and memoryview conversions
m = memoryview(b)
assert m[0] == b'a'
assert m.readonly == False
m = memoryview(c)
assert m[0] == b'a'
assert m.readonly == False
b2 = buffer(b)
assert b2[0] == b'a'
try:
    buffer(c)
except TypeError:
    pass
else:
    raise Exception("dynamic bytearray can't be a buffer")

