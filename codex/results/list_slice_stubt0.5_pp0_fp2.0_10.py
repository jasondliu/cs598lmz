import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst.append(a)
a.a=lst
keepalive.append(lst)
del a
del keepali0e
gc.collect()
print lst
print len(lst)
print gc.garbage
print len(gc.garbage)
"""

"""
import gc
class A(object):
    def __del__(self):
        print 'del'
a=A()
a.b=a
a.c=a
del a
gc.collect()
"""

"""
import gc
class A(object):
    def __del__(self):
        print 'del'
a=A()
a.b=a
a.c=a
a.d=a
a.e=a
a.f=a
a.g=a
a.h=a
a.i=a
a.j=a
a.k=a
a.l=a
a.m=a
a.n=a
a.o=a
a.p=a
a.
