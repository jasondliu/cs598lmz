import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
del keepalive
print lst
del lst
print lst

#test_weakref_callback.py
import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
r=weakref.ref(a,callback)
del a
print r
print r()
del r

#test_weakref_cycle.py
import weakref
class A(object):pass
a=A()
a.c=a
r=weakref.ref(a)
print r
print r()
del a
print r()

#test_weakref_instancemethod.py
import weakref
class A(object):pass
def f(self):pass
a=A()
r=weakref.ref(f,f)
print r
print r()
del a
print r()

#test_weakref_keyerror.py
import weakref
class A(object):pass
a=A()
r=weakref.ref(a)
print
