import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])



#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#keepalive=[]
#lst=[str()]
#a=A()
#a.c=a
#keepalive.append(weakref.ref(a,callback))
#del a
#while lst:keepalive.append(lst[:])
#del lst
#del keepalive
#import gc
#gc.collect()
#import weakref
#lst=[]
#class A(object):pass
#a=A()
#a.c=a
#a.lst=lst
#lst.append(a)
#del a
#while lst:lst.pop()
#import gc
#gc.collect()


#from __future__ import with_statement
#from contextlib import closing
#from urllib2 import urlopen
#@contextmanager
#def closing(thing):
#    try:
#        yield thing
#    finally:
#        thing.close()

