import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
lst
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a))
del a
lst
class C(object):

    def __init__(self):
        self.b=B()
