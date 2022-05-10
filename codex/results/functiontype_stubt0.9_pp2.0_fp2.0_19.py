from types import FunctionType
a = (x for x in [1])
for x in a:
    print (x)
print(x)

def fn():
    pass
print(type(fn))
print(isinstance (fn,FunctionType))

class A:
    pass

print(type(A))
print(isinstance(A,type))

a = A()
print(type(a))
print(isinstance(a,A))
