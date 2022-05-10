import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
keepalive.append(a)
keepalive.append(b)
del a
del b
lst.append(a)
lst.append(b)
del lst
gc.collect()
'''

def get_ref_info(obj):
    return (obj.__class__, weakref.getweakrefcount(obj), weakref.getweakrefs(obj))

def get_keepalive_info(obj):
    return (obj.__class__, sys.getrefcount(obj), id(obj))


def test_weakrefs():
    """Test whether weakref callbacks work with a cyclic gc"""
    class A: pass
    a = A()
    a.c = a
    wr = weakref.ref(a, callback)
    del a
    assert wr() is None


def test_finalizers():
    """Test whether __del__ methods are called with a cyclic gc"""
    class A:
        def __del__(self):
            print >> log, "
