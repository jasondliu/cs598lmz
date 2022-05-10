import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
a=None
print(lst)
from weakref import WeakKeyDictionary
class A(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'A(%s)'%self.name

d=WeakKeyDictionary()
a=A('a')
d[a]=1
print(d)
a=A('b')
print(d)
from weakref import WeakKeyDictionary
class A(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'A(%s)'%self.name

d=WeakKeyDictionary()
a=A('a')
d[a]=1
print(d)
a=A('b')
print(d)
from weakref import WeakKeyDictionary
class A(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
       
