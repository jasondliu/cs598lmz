import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#Test weakrefs on objects with a __del__ method
import weakref
class A(object):
    def __init__(self):
        self.b=B(self)
    def __del__(self):
        pass
class B(object):
    def __init__(self,a):
        self.a=a
    def __del__(self):
        pass
a=A()
r=weakref.ref(a)
del a
del r

#Test weakrefs on objects with a __del__ method
import weakref
class A(object):
    def __init__(self):
        self.b=B(self)
    def __del__(self):
        pass
class B(object):
    def __init__(self,a):
        self.a=a
    def __del__(self):
        pass
a=A()
r=weakref.ref(a)
del a
del r

#Test weakrefs on objects with a __del__ method
import weakref
class A(object):
    def __
