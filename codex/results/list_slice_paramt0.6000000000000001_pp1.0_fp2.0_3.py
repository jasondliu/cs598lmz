import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback)
del a
keepali0e.append(weakref.ref(lst[0],callback))
print len(lst)
del lst
print len(keepali0e)
for i in keepali0e:
    print i
"""

"""
import weakref
class A(object):pass
class B(object):pass
def callback(x):print 'callback'
a=A()
b=B()
a.b=b
b.a=a
weakref.ref(a,callback)
del a
del b
"""

"""
import weakref
class A(object):
    def __init__(self):
        print 'init'
    def __del__(self):
        print 'del'
def callback(x):print 'callback'
a=A()
print weakref.ref(a,callback)
del a
"""


"""
import weakref
class A(object):
    def __init__(self):
        print 'init'
    def __del__(self):
        print 'del'
def callback(x
