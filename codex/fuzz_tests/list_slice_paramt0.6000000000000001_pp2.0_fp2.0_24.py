import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del a.c
del keepali0e
del lst

def test2():
    import weakref
    class A(object):pass
    def callback(x):del lst[0]
    keepali0e=[]
    lst=[str()]
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
    keepali0e.append(weakref.ref(a.c,callback))
    del a
    del a.c
    del keepali0e
    del lst

###

# test3
class A(object):
    def __init__(self):
        self.b=B()
        self.b.a=self
class B(object):pass
def test3():
    class A(object):
        def __init__(self):
            self.b=B()
            self.b.a=self
    class B(object):pass
