import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)
print keepali0e
print lst
print lst[0]
"""
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)
print keepali0e
print lst
print lst[0]

"""
keepalive=[]
lst=[str()]
def callback(x):del lst[0]
class A(object):
    def __init__(self):
        self.c=self
        keepalive.append(weakref.ref(self,callback))
a=A()
del a
print len(lst)
print keepalive
print lst
print lst[0]

keepalive=[]
lst=[str()]
def callback(x):del lst[0]
class A(object):
    def __init__(self):
        self.c=self
        keepalive.append(weakref.ref(self,callback))
a=A
