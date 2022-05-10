from types import FunctionType
a = (x for x in [1])
print(type(a))

b= FunctionType(a,1,5) # The returned function object is an iterator
print(type(b))
print(next(b))
print(next(b)) # will throw StopIteration:

def foo():
    print('hello world')

foo.x=1
print(type(foo))
123 + foo
456 - foo
print(type( foo.x))



print(type(foo.__name__))
print(type(foo.__annotations__))
print(type(foo.__closure__))
print(type( foo.__code__))
print(type(foo.__defaults__))
print(type(foo.__dict__))
print(type(foo.__globals__))
print(type(foo.__get__))
print(type(foo.__globals__))
print(type(foo.__kwdefaults__))
print(type(foo.__module__))
print(type(foo.__name__))
print(type(foo.__qualname__))
print
