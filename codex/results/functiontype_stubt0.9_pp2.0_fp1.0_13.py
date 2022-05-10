from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))
print(isinstance(a, object))

############### And this is the function, which the generator is wrapping:
def d():
    """Gaaaaaaaaaarbage"""
    yield 1


print(isinstance(d, Generator))
print(isinstance(d, FunctionType))
print(isinstance(d, object))
print(isinstance(d(), Generator))
print(isinstance(d(), FunctionType))
print(isinstance(d(), object))

############# More and more confusion:
def c():
    return 1

def d():
    yield 1

def e():
    yield from [1,2]

def f():
    yield from (x**2 for x in [1,2])

print(callable(c))
print(callable(d))
print(callable(e))
print(callable(f))

#############  I couldn't come up with a way to generate a callable generator

class A
