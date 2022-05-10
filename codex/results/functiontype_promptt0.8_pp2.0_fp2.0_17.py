import types
# Test types.FunctionType(function, globals, name, argdefs, closure)
def f1(a):
    return a

def f2(a,b):
    return a+b

def f3(a,b,c):
    return a+b+c

def f4(a=0,b=0,c=0):
    return a+b+c

def f5(a,b,c=0):
    return a+b+c

def f6(a,b,*args):
    return a+b+sum(args)

def f7(a,b,c=0,*args):
    return a+b+c+sum(args)

def f8(a,b,*args,**kwargs):
    return a+b+sum(args)+sum(kwargs.values())

def f9(a,b,c=0,*args,**kwargs):
    return a+b+c+sum(args)+sum(kwargs.values())

def f10(*args,**kwargs):
    return sum
