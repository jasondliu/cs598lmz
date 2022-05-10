import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
lst[0]=a
keepalive.append(lst)
weakref.ref(a,callback)
del a

#reference cycle.

#7.1.1
#import weakref
#class A(object):pass
#a=A()
#weakref.ref(a)
#del a

#7.1.2
from weakref import *
from gc import collect
class A(object):pass
a=A()
r=ref(a)
print r
collect()
print r

#7.1.3
from weakref import *
from gc import collect
class A(object):pass
a=A()
r=ref(a,lambda x:print 'deleted')
print r
del a
collect()

#7.1.4
from weakref import *
from gc import collect
class A(object):pass
a=A()
r=ref(a,lambda x:print 'deleted')
print r
del a
print r
collect()

#7
