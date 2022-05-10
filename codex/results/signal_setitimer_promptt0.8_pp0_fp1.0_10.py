import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)

class C:
    def the_meth(self):
        return 42
    def f():
        return 42

def f():
    return 42

def g(a,b,c=None,d=None):
    return a+b

def h(a,b=None,c=None):
    return a+b

def i(a,b,*args,d=None):
    return a+b

def j(a,b,c=42,**args):
    return a+b+c

def k(a,b,*args,d=42,**kwargs):
    return a+b+d

def l(a,b,*args,c=42,**kwargs):
    return a+b+c

def m(a,b=42,*args,**kwargs):
    return a+b

# Test unpacking generators

def u():
    yield 1
    yield 2
    yield 3


