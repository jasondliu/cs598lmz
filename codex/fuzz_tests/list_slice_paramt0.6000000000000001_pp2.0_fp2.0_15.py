import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
lst[0]

lst=[str()]
a=A()
keepali0e.append(weakref.ref(a, callback))
del a
lst[0]

class A(object):
    __slots__=['a']
    def __init__(self):self.a=1
    def __weakref__(self):
        return weakref.ref(self.a, callback)

a=A()
keepali0e.append(weakref.ref(a, callback))
lst[0]

del a
lst[0]

lst=[str()]
a=A()
keepali0e.append(a)
del a
lst[0]

class A(object):
    __slots__=['__weakref__']
    def __init__(self):pass

a=A()
keepali0e.append(weakref.ref(a, callback))
del a
lst[0]

lst=[str()]
a=A()
keep
