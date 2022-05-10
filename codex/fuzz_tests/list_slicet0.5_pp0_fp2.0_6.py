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
keepali0e[0]()
print keepali0e
print len(keepali0e)
print lst

print '\n'
print '-'*30
print '\n'

import gc
import weakref
class A(object):pass
def callback(x):print 'callback'
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
del keepali0e[:]
gc.collect()
print keepali0e
print len(keepali0e)
print lst
