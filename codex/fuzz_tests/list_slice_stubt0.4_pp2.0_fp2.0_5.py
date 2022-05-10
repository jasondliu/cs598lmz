import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
del a
del keepalive
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
del lst
del keepalive
del callback
del weakref
del A
del str
del x
""")

def test_memory_leak_in_weakref_callback():
    import gc
    import weakref
    class A(object):pass
    def callback(x): del lst[0]
    keepalive = []
    lst = [str()]
    a = A()
    a.c = a
    keepalive.append(a)
    keepalive.append(lst)
    del a
    del keepalive
    lst.append(a)
    lst.append(weakref.ref(a, callback))
    del a
    del lst
    del keepalive
    del callback
    del weakref
    del A
    del str
    del x
    gc.
