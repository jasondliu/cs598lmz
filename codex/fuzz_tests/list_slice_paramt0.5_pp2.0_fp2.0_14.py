import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
'''

def test_weakref_callback():
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
    lst.append(a)
    del a

def test_weakref_callback_2():
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
    lst.append(a)
    del a
    assert len(lst) == 1

def test_weakref_callback_3():
    import weakref
    class A(object):
        pass
