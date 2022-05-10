from types import FunctionType
a = (x for x in [1])
print(type(a))

b = lambda x:x+1
print(type(b))

c = FunctionType(b.__code__, b.__globals__, name=b.__name__, argdefs=b.__defaults__, closure=b.__closure__)
print(type(c))
print(b.__dict__)
print(c.__dict__)
print(c.__code__.__dict__)
print(c.__closure__)
print(c.__closure__[0].cell_contents)
