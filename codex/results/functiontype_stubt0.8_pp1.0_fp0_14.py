from types import FunctionType
a = (x for x in [1])
b = (1,)

print(type(a), type(b), a, b)

print(type(b) == tuple, type(b) == tuple)

print([1] is [1], [1] == [1])

print(id(a), id(b))
print(id(type(a)), id(type(b)))
print(type(type(a)) is type)
print(isinstance(a, GeneratorType))
print(isinstance(sum, FunctionType))

print(dir(a), sum.__name__)

class C:
    def __init__(self, x):
        self.x = x

c = C(1)
print(type(c), c.x)

# 对象的三大属性

# 闭包
def f(x):
    def g(y):
        return x + y
    return g

def f2(x):
    def g2(y):
        nonlocal x
        x += y
        return x
    return
