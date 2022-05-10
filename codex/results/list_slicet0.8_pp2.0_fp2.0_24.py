import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e[-1])

import gc
def collect():
    print("collecting")
    n=gc.collect()
    print("unreachable objects:",n)
    print("garbage:",gc.garbage)

gc.disable()
print("gc enabled:",gc.isenabled())

collect()
lst=[]
lst.append(lst)
collect()

class Applier:
    def __init__(self,func,args,kwds):
        self.func=func
        self.args=args
        self.kwds=kwds
    def __call__(self):
        return self.func(*self.args,**self.kwds)

def apply_async(func,args=None,kwds=None,callback=None):
    if callback is None:
        result=Applier(func,args or (),kwds or {})
    else:
        def wrapper(*args,**kwds):
            callback(func(*args,**kwds))
        result=Applier(wrapper,args,
