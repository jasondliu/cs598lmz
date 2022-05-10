import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w1=weakref.ref(a,callback)
a=None
assert len(lst)==1,"reference count leak"
try:
    from ctypes import pythonapi
except ImportError:
    pass
else:
    pythonapi.Py_SetAllocator(3,None)
class C:pass
class C2(C):pass
class C3(C):pass
def f(x):
    if x:
        c2=C2
    else:
        c2=C3
    for i in range(100):c2()
def g():
    for i in range(100):C()
def h():
    for i in range(100):C2()
def i():
    for i in range(100):C3()
import gc
def run(func):
    gc.collect()
    gc.set_threshold(200,1,1)
    func()
    return gc.collect()
print(run(f),
run(g),
run(h),
run(i))
