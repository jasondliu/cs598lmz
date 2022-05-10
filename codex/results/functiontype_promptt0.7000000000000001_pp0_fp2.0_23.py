import types
# Test types.FunctionType and types.LambdaType
print(types.FunctionType is types.LambdaType)
print(lambda x: x is lambda y: y)
print(lambda x: x is lambda y: y())
print(lambda x: x() is lambda y: y())
print(lambda x: x is lambda y: y())

# Test type annotations
print(lambda x: x)

def f1(a,b,c):
    print(a,b,c)

def f2(*args):
    print(args)

def f3(**kwargs):
    print(kwargs)

def f4(*args, **kwargs):
    print(args)
    print(kwargs)

def f5(a,b,c=0,d=0,*args,**kwargs):
    print(a,b,c,d,args,kwargs)

def f6(a,b,c=0,d=0,*args,e,f=0,**kwargs):
    print(a,b,c,d,args,e
