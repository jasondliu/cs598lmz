from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = {'a':1,'b':2}
d = 1
e = FunctionType
f = type

g = (1,)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

print('--'*30)
print(isinstance(a,GeneratorType))
print(isinstance(b,GeneratorType))
print(isinstance(c,GeneratorType))
print(isinstance(d,GeneratorType))
print(isinstance(e,GeneratorType))
print(isinstance(f,GeneratorType))
print(isinstance(g,GeneratorType))

print('--'*30)
print(isinstance(a,list))
print(isinstance(b,list))
print(isinstance(c,list))
print(isinstance(d,list))
print(isinstance(e,list))
print(isinstance(f,list))
