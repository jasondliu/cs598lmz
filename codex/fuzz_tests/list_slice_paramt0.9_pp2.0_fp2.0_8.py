import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepalive=1

class C(A):pass
a.c=C()
keepalive=2
del a.c
keepalive=3


from weakref import WeakKeyDictionary
class MyClass:
    def __init__(self, name):
        self.name=name
d=WeakKeyDictionary()
o=MyClass('A')
d[o]=1
keepalive=o

b=keepalive

from weakref import WeakValueDictionary
class MyClass:
    def __init__(self, name):
        self.name=name
d=WeakValueDictionary()
d['a']=keepalive
o=MyClass('A')
d[1]=o
keepalive=o

b=keepalive

from weakref import WeakSet
lst=[1,2,3]
s=WeakSet(lst)
s
s.data
s.weakrefs
s.count()
keepalive=s


del lst[1]
keepalive.count()
keep=
