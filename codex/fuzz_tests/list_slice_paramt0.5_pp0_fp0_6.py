import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
gc.collect()
print('lst=%r'%lst)

print('\n\n')
import weakref,gc
class A(object):pass
def callback(x):print('callback called')
a=A()
keepali0e=weakref.ref(a,callback)
del a
gc.collect()

print('\n\n')
import weakref
class A(object):pass
a=A()
a.c=a
keepali0e=weakref.ref(a)
keepali0e.c=keepali0e
del a
print(keepali0e.c())
print(keepali0e())

print('\n\n')
import weakref
class A(object):pass
a=A()
a.c=a
keepali0e=weakref.ref(a)
keepali0e.c=keepali0e
del a
import gc
print(gc.get_referents
