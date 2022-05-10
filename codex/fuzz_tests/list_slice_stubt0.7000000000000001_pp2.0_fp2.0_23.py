import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=weakref.ref(a,callback)
del a
gc.collect()

#weakref with a callback
import weakref
class A(object):pass
def callback(x):
    print 'callback called'
    print x
a=A()
a.c=a
keepalive=weakref.ref(a,callback)
del a
gc.collect()
print 'end of program'

#weakref with a callback, and self-referencing list
#the callback will be called after the list is deallocated
import weakref
class A(object):pass
def callback(x):print 'callback called'
a=A()
a.c=a
keepalive=weakref.ref(a,callback)
del a
lst=[str()]
lst.append(lst)
keepalive=lst
del lst
gc.collect()
print 'end of program'


#weakref without a callback
import weakref
class A(object):pass
a=A()
a.c=a
keepalive=weakref.
