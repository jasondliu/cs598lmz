import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
b=weakref.ref(a,callback)
del a
print(lst)
c=A()
c.c=c
keepalive.append(c)
d=weakref.ref(c,callback)
del c
print(lst)

'''

'''
import weakref
class A(object):pass
a=A()
a.c=a
b=weakref.ref(a,lambda x:print(x))
del a
print(b())

'''

'''
import weakref
class A(object):pass
a=A()
a.c=a
b=weakref.ref(a,lambda x:print(x))
del a
print(b())

'''

'''
import weakref
class A(object):pass
a=A()
a.c=a
b=weakref.ref(a,lambda x:print(x))
del a
print(b())

'''

'''
import weakref
class A(object):pass
