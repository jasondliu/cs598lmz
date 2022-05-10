import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

#2
from weakref import WeakKeyDictionary
class A(object):
    _dict=WeakKeyDictionary()
    def __init__(self):
        self._dict[self]=str()
    def __del__(self):
        del self._dict[self]

#3
from weakref import WeakKeyDictionary
class A(object):
    dict=WeakKeyDictionary()
    def __init__(self):
        self.dict[self]=str()
    def __del__(self):
        del self.dict[self]

#4
from weakref import WeakKeyDictionary
class A(object):
    dict=WeakKeyDictionary()
    def __init__(self):
        self.dict[self]=str()
    def __del__(self):
        del self.dict[self]

#5
from weakref import WeakKeyDictionary
class A(object):
    dict=WeakKeyDictionary()
    def __init__(self):
        self.dict[self]=str()
    def __del
