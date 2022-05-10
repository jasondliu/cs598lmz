import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
keepali0e.append(weakref.ref(a,callback))
print len(keepali0e)
del a
del lst
print len(keepali0e)

print '\n\n'

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
keepali0e.append(weakref.ref(a,callback))
print len(keepali0e)
del a
del lst
print len(keepali0e)
