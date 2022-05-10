import types
types.SimpleNamespace(a=1, b=2)

f = types.SimpleNamespace()
f.name = 'bob'
f.age = 40

types.SimpleNamespace()

# ------------------------------------------------
x = 'hello'
x_iter = iter(x)
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))

# ------------------------------------------------

x = 5
print(x)
print(id(x))
y = 5
print(y)
print(id(y))

x = -6.0
print(x)
print(id(x))
y = -6.0
print(y)
print(id(y))

x = 'hello'
y = 'hello'
print(x == y)
print(x is y)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

x = (1
