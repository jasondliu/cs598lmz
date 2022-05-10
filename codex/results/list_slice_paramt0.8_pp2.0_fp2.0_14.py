import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
try:
    x=1
finally:
    del a.c
    a=None
    gc.collect()
    assert not lst
gc.collect()
