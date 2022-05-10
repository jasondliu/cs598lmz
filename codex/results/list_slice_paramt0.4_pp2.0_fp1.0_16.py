import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

import weakref
class A(object):
    def __del__(self):
        print 'A.__del__'
def callback(x):
    print 'callback'
    print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e

import weakref
class A(object):
    def __del__(self):
        print 'A.__del__'
def callback(x):
    print 'callback'
    print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e()

import weakref
class A(object):
    def __del__(self):
        print 'A.__del__'
def callback(x):
    print 'callback'
    print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e
