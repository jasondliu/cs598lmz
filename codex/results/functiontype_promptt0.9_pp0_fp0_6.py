import types
# Test types.FunctionType
def test():
    return None

print(type(test) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
test()
def fn(self,name='world'):
    print('hello %s'%name)

Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
h.hello()

print(type(h))

def fn(self):
    raise ImportError

def fn1(self):
    pass

try:
    fn(fn1)
except ImportError:
    pass

def fn2(self,name='world'):
    print('Hello,%s.'%name)

Hello1=type('Hello',(object,),dict(hello=fn2))
h2=Hello1()
h2.hello()

print(type(h2))
print(type(Hello1))



