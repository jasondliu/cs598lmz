import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print lst
print keepalive
'''

'''
#weakref.proxy()
import weakref
class A(object):pass
lst=[str()]
a=A()
a.c=a
lst.append(a)
p=weakref.proxy(a)
print p.c
print lst
del a
print p.c
print lst
'''

'''
#weakref.proxy(obj)
class A(object):pass
lst=[str()]
a=A()
a.c=a
lst.append(a)
p=weakref.proxy(a)
print p.c
print lst
del a
print p.c
print lst
'''

'''
#weakref.proxy(obj,callback)
import weakref
class A(object):pass
lst=[str()]
a=A()
a.c=a
lst.append(a)
p
