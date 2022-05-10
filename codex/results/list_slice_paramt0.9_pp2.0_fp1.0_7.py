import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepref=str('keep a alive')
del a,keepali0e,lst
gc.collect()
import weakref
class A(object):pass
a=A()
a.c=a
keepref=str('keep a alive ')
def callback(x):print(x)
wb=weakref.ref(a,callback)
del a
del keepref
gc.collect()
import weakref
class A(object):pass
a=A()
keepref=str('keep a alive ')
def callback(x):print(x)
wb=weakref.ref(a,callback)
a.c=wb
del keepref
del a
gc.collect()
import weakref
class A(object):pass
a=A()
keepref=str('keep a alive ')
def callback(x):print(x)
wb=weakref.ref(a,callback)
a.c=wb
del keepref
del a
gc.collect()
