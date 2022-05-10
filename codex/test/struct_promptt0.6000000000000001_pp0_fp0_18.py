import _struct
# Test _struct.Struct()

a = _struct.Struct('hhl')
b = _struct.Struct('hhl')

c = _struct.Struct('hhl')
c = c.__new__(c)

print(a)
print(b)
print(c)

print(a.size)
print(b.size)
print(c.size)
