import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst.append(A())
lst.append(A())
del a
del lst[0]
del lst[0]
del lst[0]
del keepali0e[0]
del lst
del keepali0e
''')

def test_weakref_callback():
    import _weakref, gc
    class A:
        def __init__(self):
            self.nr = 0
        def __del__(self):
            self.nr = -1
    a = A()
    lst = []
    def callback(x):
        lst.append(1)
    wr = _weakref.ref(a, callback)
    assert wr() is a
    del a
    gc.collect()
    assert lst == [1]
    assert wr() is None
    wr = _weakref.ref(a, callback)
    assert wr() is None
    assert lst == [1]

def test_weakref_callback_exception():
    import _weakref, gc
   
