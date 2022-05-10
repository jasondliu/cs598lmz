from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a,FunctionType))

class Foo:
    def __init__(self,name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print(self.name)
        print(args,kwargs)

f = Foo('Alex')
print(type(f))
print(isinstance(f,FunctionType))
print(f())
