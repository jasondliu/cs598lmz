from types import FunctionType
list(FunctionType(x, globals(), 'foo')(1, 2, 3) for x in [lambda x, y, z: x + y + z, lambda x, y, z: x * y * z])

#another:
def foo(x, y, z):
    return x + y + z

def bar(x, y, z):
    return x * y * z

list(g(1, 2, 3) for g in [foo, bar])
</code>

