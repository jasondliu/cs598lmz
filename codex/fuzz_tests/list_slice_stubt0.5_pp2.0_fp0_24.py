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
print len(lst)
print lst[0]
print keepalive[0].c

#2
print '\n'
keepalive=[]
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print len(lst)
print lst[0]
print keepalive[0].c

#3
print '\n'
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
del a
print len(lst)
print lst[0]

#4
print '\n'
import weakref
class A(object
