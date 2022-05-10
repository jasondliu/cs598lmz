from types import FunctionType
a = (x for x in [1])
print(type(a))

def foo():
    pass
print(type(foo))

print(isinstance(foo, FunctionType))
print(isinstance(a, FunctionType))

print(isinstance(foo, object))
print(isinstance(a, object))

print(isinstance(foo, Iterator))
print(isinstance(a, Iterator))

print(isinstance(foo, Iterable))
print(isinstance(a, Iterable))

print(isinstance(foo, Generator))
print(isinstance(a, Generator))

print(isinstance(foo, GeneratorExp))
print(isinstance(a, GeneratorExp))


# In[ ]:
