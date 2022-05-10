import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
del a
keepalive.append(lst)
gc.collect()
lst.append(str())
del lst[1]
gc.collect()
keepalive.append(lst)
gc.collect()
del keepalive[0]
gc.collect()
del keepalive[0]
gc.collect()
print("OK")
"""

def test_gc_callback():
    import gc

    def callback(i):
        print("callback", i)

    class Foo:
        pass

    f1 = Foo()
    f2 = Foo()
    f1.callback = callback
    f2.callback = callback
    gc.collect()
    gc.callbacks.append(f1.callback)
    gc.callbacks.append(f2.callback)
    gc.collect()
    del f1
    del f2
    gc.collect()

"""
import gc
def callback(x):print("callback")
class Foo:pass
f1=Foo()
f2=
