from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

print(dir(a))
print(dir(a.__next__))

print(a.__next__.__name__)
print(a.__next__.__qualname__)
print(a.__next__.__module__)
print(a.__next__.__code__)
print(a.__next__.__defaults__)
print(a.__next__.__kwdefaults__)
print(a.__next__.__closure__)
print(a.__next__.__annotations__)
print(a.__next__.__globals__)
print(a.__next__.__dict__)
print(a.__next__.__self__)
print(a.__next__.__func__)
print(a.__next__.__get__)
print(a.__next__.__text_signature__)
print(a.__next__.__
