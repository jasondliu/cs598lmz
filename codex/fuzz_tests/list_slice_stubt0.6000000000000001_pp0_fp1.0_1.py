import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
w=weakref.ref(a,callback)
del a
del keepalive
print lst

"""
class A(object): pass
def callback(x): print 'callback called'
a = A()
a.c = a
w = weakref.ref(a, callback)
del a
print w
print w()
"""

"""
class A(object): pass
def callback(x): print 'callback called'
a = A()
a.c = a
w = weakref.ref(a, callback)
del a
print w
print w()
"""

"""
class A(object): pass
def callback(x): print 'callback called'
a = A()
a.c = a
w = weakref.ref(a, callback)
del a
print w
print w()
"""

"""
class A(object): pass
def callback(x): print 'callback called'
a = A()
a.c = a
w = weakref.ref(a, callback)
del a
print w
print w()
"""

