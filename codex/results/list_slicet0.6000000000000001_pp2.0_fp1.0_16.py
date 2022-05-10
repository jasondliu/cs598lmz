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
'''

def test_leak_ref_cycle_with_callback():
    import gc
    import weakref

    class A(object):
        pass

    def callback(x):
        del lst[0]

    keepalive = []
    lst = [str()]
    a = A()
    a.c = a
    keepalive.append(weakref.ref(a, callback))
    del a
    while lst:
        keepalive.append(lst[:])
    gc.collect()


class AppTestWeaksets:
    spaceconfig = {
        "usemodules": ("_weakref", "itertools"),
    }

    def setup_class(cls):
        # run the test many times so that we can see the effect of
        # the weakref callbacks getting called or not getting called
        cls.w_runs = cls.space.wrap(5)

    def test_basic(self):
        import weakref
        class A(object): pass
        a = A()
        r = weak
