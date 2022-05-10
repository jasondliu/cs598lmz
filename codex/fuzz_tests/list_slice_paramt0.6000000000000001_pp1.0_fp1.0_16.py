import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
lst[0]=a
del a
lst[0].c=lst[0]
del lst[0].c
lst[0].c=lst[0]
del lst[0].c
'''

def test_gc_collect_with_weakrefs(self):
    import _weakref
    class A(object):
        pass
    def callback(x):
        del lst[0]
    keepalive = []
    lst = [str()]
    a = A()
    a.c = a
    keepalive.append(weakref.ref(a))
    keepalive.append(weakref.ref(a.c))
    lst[0] = a
    del a
    del lst[0].c
    lst[0].c = lst[0]
    del lst[0].c
    lst[0].c = lst[0]
    del lst[0].c
    import g
