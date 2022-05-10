import types
# Test types.FunctionType
def foo(x):
    return x

def bar(x):
    return x

def baz(x=1):
    return x

def qux(x,y=2):
    return x,y

def quux(x,y=2,*args):
    return x,y,args

def quuz(x,y=2,*args,**kwargs):
    return x,y,args,kwargs

def corge(x,y=2,*args,bar,**kwargs):
    return x,y,args,bar,kwargs

def grault(x,y=2,*args,bar,baz=3,**kwargs):
    return x,y,args,bar,baz,kwargs

def garply(x,y=2,*args,bar,baz=3,**kwargs):
    return x,y,args,bar,baz,kwargs

def waldo(x,y=2,*args,bar,baz=3,**kwargs):
    return x,
