from types import FunctionType
a = (x for x in [1])
b = a.throw(TypeError('x'))
print(type(b))

def func():
    try:
        yield
    except TypeError as e:
        print(type(e))
        print(type(e) == TypeError)
        print(e)

c = func()
print(type(c))
print(isinstance(c, FunctionType))
next(c)
c.throw(TypeError('x'))

print('----------------------')

try:
    raise TypeError('x')
except TypeError as e:
    print(type(e) == TypeError)
    print(e)

print('----------------------')

try:
    raise TypeError('x') from None
except TypeError as e:
    print(e)
    print(e.__context__)
    print(e.__suppress_context__)

print('----------------------')

try:
    raise TypeError('x') from None
except TypeError as e:
    try:
        raise TypeError('y') from e
    except TypeError as
