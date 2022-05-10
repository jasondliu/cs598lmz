import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
keepali0e.append(weakref.ref(lst[0],callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del lst
import gc
gc.collect()
print keepali0e[0]()
print keepali0e[1]()
print keepali0e[2]()
print keepali0e[3]()

#2.
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
keepali0e.append(weakref.ref(lst[0],callback))
keepali0e.append(weakref.ref(a.c,callback))
lst[0]="aa"
del
