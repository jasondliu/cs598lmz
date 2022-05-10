import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)
weakref.ref(a,callback)
del a
keepalive.append(lst)
print len(lst)
print lst
print keepalive
"""
"""
import weakref
class A(object):pass
class B(object):pass
def callback(x):
    del lst[0]
    print 'callback'
b=B()
a=A()
a.b=b
a.c=a
a.d=a
lst=[str()]
keepalive=[a,lst]
weakref.ref(a,callback)
del a
print 'lst',lst
print 'keepalive',keepalive
"""
"""
import weakref
class A(object):
    def __init__(self,arg):
        self.arg=arg
        print 'init',self.arg
    def __del__(self):
        print 'del',self.arg
def callback(x):
    print 'callback',x()
    del lst[0]
a
