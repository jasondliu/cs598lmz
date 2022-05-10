import types
types.GeneratorType

# type has a metclass of type
type(type)

# only classes and modules have metaclasses
t = type(int)
t.__class__

# class foo has a metaclass of type
class foo: pass
f = foo()
print(type(foo))
print(type(f))

print(type.__class__)
print(type(type.__class__))

# print(type(object))
# print(type(object.__class__))

# type(type(type))  # <type 'type'>
