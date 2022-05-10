import types
types.new_class('Vector', (list,))

Vector([1, 2, 3])

v = Vector([1, 2, 3])
print(type(v))
print(v.__class__)
