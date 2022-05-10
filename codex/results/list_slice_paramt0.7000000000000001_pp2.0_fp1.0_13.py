import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(lst[0],callback))
del a
del keepali0e
lst[0]='foo'
print lst
print lst[0]
"""
"""
import weakref
class A(object):
    def __init__(self):
        self.keepalive=[]
        self.keepalive.append(weakref.ref(self,self._callback))
    def _callback(self,w):del self.keepalive[:]
a=A()
del a
"""
"""
import weakref
class A(object):
    def __init__(self):
        self.keepalive=[]
        self.keepalive.append(weakref.ref(self,self._callback))
    def _callback(self,w):del self.keepalive[:]
a=A()
del a
a=A()
del a
"""
"""
import weakref
class A(object):
    def
