import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
if len(keepali0e):print 'FAIL:callback not called'
else:print 'OK'
del keepali0e
del lst
del callback
del weakref
del A
del a
print '\n'
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
if len(keepali0e):print 'FAIL:callback not called'
else:print 'OK'
del keepali0e
del lst
del callback
del weakref
del A
del a
print '\n'
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
if len(
