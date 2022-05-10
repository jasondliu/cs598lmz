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
"""
"""
class A(object):__slots__=()
from __builtin__ import property,object
def getx(self):return self.__x
def setx(self,value):self.__x=value
prop=property(getx,setx,doc='I am the x property')
class A(object):
    x= prop
def l(x):
    A.x=x
    print A.x
l("hello")
from __builtin__ import delattr,getattr
class A(object):pass
delattr(A,'x')
class A(object):
    def g(self):return 5
    def _p(self):pass
x=A()
getattr(x,'g')
getattr(x,'_p').__doc__
class A(object):
    def _p(self):pass
class B(object):
    def _p(self):pass
    p = A._p
x = A()
getattr(x,'_p').im_func is A._p
B.p.im_func is A._p
"""
