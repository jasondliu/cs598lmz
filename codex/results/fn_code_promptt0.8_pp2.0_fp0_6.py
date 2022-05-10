fn = lambda: None
# Test fn.__code__.co_varnames[:fn.__code__.co_argcount]

def f1(): pass
def f2(x): pass
def f3(a,b): pass
def f4(a=1,b=2,c=3): pass
def f5(a,b=2,c=3): pass
def f6(a,b,c=3): pass
def f7(*args,**kwargs): pass
def f8(a,*args,**kwargs): pass
def f9(a,b,*args,**kwargs): pass
def f10(a,b,c=3,*args,**kwargs): pass
def f11(a,b,c=3,*args,d,**kwargs): pass
def f12(a,b,c=3,*args,d=4,**kwargs): pass
def f13(a,b=2,c=3,*args,d,**kwargs): pass
def f14(a,b=2,c=3,*args,d=4,**kwargs
