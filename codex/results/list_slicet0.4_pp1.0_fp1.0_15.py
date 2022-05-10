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

#test_weakref_callback_with_instancemethod
import weakref
class A(object):
    def __init__(self):
        self.lst=[]
    def callback(self,x):
        self.lst.append(x)
a=A()
keepali0e=[]
for i in range(10):
    keepali0e.append(weakref.ref(str(),a.callback))
del a

#test_weakref_callback_with_staticmethod
import weakref
class A(object):
    @staticmethod
    def callback(x):
        del lst[0]
lst=[str()]
keepali0e=[]
for i in range(10):
    keepali0e.append(weakref.ref(str(),A.callback))
del A
while lst:keepali0e.append(lst[:])

#test_weakref_callback_with_classmethod
import weakref
class A(object):
    @classmethod
    def callback(cls,x):
        del lst[
