from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])

isinstance(a, FunctionType)

print(a)
print(b)

# a.__next__()
# a.__next__()

print(a.send(None))
print(a.send(None))


print(b.send(None))
print(b.send(None))

print(a.send(None))
print(b.send(None))

print(a.send(None))
print(b.send(None))
