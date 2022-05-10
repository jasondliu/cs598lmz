from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = (x for x in [1])
d = (x for x in [1])
e = (x for x in [1])
f = (x for x in [1])
g = (x for x in [1])

# ok
print(id(a), id(b))

# ok
print(hash(a), hash(b))

# ok
print(repr(a), repr(b))

# ok
print(a, b)

# ok
print(a == b)

# ok
print(a != b)

# ok
print(a is b)

# ok
print(a is not b)

# ok
print(a in b)

# ok
print(a not in b)

# ok
print(a > b)

# ok
print(a < b)

# ok
print(a >= b)

# ok
print(a <= b)

# ok
print(a == 0)

# ok
print(a !=
