import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
b=A()
b.c=a
keepali0e.append(weakref.ref(b))
lst.append(b)
keepali0e.append(weakref.ref(lst,callback))
a=None
b=None
lst=None
import gc;gc.collect()
print keepali0e
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keepali0e[2]()
print keep
