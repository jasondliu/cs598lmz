from types import FunctionType
a = (x for x in [1])
b = lambda :1
print(type(a))
print(type(b))
print(type(lambda :1))
print(type(lambda x:x))
print(type(lambda x:x*x))
print(type(lambda x,y:x*y))
print(type(lambda x,y,z:x*y*z))
print(type(lambda x,y,z,w:x*y*z*w))
