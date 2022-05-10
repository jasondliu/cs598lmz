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
if sys.version_info[:2]<(2,7):
    try:
        import __pypy__
        import gc
        gc.collect()
    except ImportError:
        pass
try:
    import ctypes
    ctypes.cdll.msvcrt.get_throttle()
except:
    pass

__all__=[]
class BaseTest(object):

    def setup_class(cls):
        global lst
        lst=[]

    def test_append_delete(self):
        global lst
        a=A()
        lst.append(a)
        del a
        while lst:keepali0e.append(lst[:])

    def test_append_pop(self):
        global lst
        a=A()
        lst.append(a)
        del lst[:]
        while lst:keepali0e.append(lst[:])

    def test_create(self):
        global lst
        del lst[:]
        while lst:keepali
