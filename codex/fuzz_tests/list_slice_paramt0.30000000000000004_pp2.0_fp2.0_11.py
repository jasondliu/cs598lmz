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
lst[0]='a'
del lst
import gc
gc.collect()
print keepali0e
print len(keepali0e)
print keepali0e[0]()
print keepali0e[1]()
print keepali0e[0]() is keepali0e[1]()
print keepali0e[0]() is keepali0e[1]()
print keepali0e[0]() is keepali0e[1]()
print keepali0e[0]() is keepali0e[1]()
print keepali0e[0]() is keepali0e[1]()
print keepali0e[0]() is keepali0e[1]()
print keepali0e[0]() is keepali0e[1]()
print keepali0e[0]() is keepali0e[1]()
print keepali0e[0]() is keepali0e[1]()

