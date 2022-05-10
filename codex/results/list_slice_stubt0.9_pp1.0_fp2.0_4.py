import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=None
keepalive=[]
for _ in xrange(100):del _
_keepalive = keepalive
del keepalive, _keepalive

def f(): pass
def g(): print("suppression d'un objet")
    f()
keepalive = []
for i in xrange(10000):
    l = [str() for j in xrange(25)]
    wr = weakref.ref(l, g)
    keepalive.append((wr, l))
del keepalive

def tamper(kwd):
    return kwd.copy()
def s(): print("suppression d'un objet")
def g(): print("garbage collector inspection")
    s()
def get_locals():
    frame = inspect.currentframe()
    try:
        try:
            return frame.f_back.f_locals
        finally:
            del frame
    except RuntimeError: 
        try:
            return tamper(frame.f_back.f_locals)
        finally:
            del frame
