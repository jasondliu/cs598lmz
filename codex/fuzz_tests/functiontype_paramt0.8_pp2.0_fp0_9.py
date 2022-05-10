from types import FunctionType
list(FunctionType(lambda x:x+x,'foo'))

print([FunctionType({1:2},(1,2,3),(4,5,6))]) # [<function <lambda> at 0xb7dce28c>]

a=object()
print(a==a) # True
print(a is a) # True
print(id(a)) # 140524688509920
print(id(a)==id(a)) # True
#print(id(a) is id(a)) # False 

type(a) is type(a)  # True
a is a # True

def f(a):
    def g(b):
        def h(c):
            print(type(h))
            return a+b+c
    return h
print(f(1)(2)(3))

class X:
    def __init__(self,a):
        print(type(self))
        print(type(X))
    def __call__(self,b):
        print(type(self))
        print(type(X))
        return
