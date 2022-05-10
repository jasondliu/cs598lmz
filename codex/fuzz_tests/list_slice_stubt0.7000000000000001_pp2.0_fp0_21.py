import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
sys.getrefcount(a)
del a
sys.getrefcount(a)
del keepalive
sys.getrefcount(a)
del lst
sys.getrefcount(a)
x=A()
y=weakref.ref(x,callback)
y()
del x
del y
import weakref
def f(x):
    return x**2

a=weakref.WeakKeyDictionary()
b=weakref.WeakValueDictionary()
a[1]=f
b[f]=1
print a[1](2)
print b[f]
del f
print a[1](2)

b[3]

import weakref
class Test(object):
    def __del__(self):
        print 'deleted'

class ExpiringTest(object):
    def __init__(self,callback):
        self.callback=callback
    def __del__(self):
        self.callback()

def create_test():
    return Test()
x=ExpiringTest(create_
