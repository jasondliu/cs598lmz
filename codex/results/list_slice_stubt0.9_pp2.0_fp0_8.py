import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepali0e.append(a)
keepali0e.append(a.a)
keepali0e.append(a.b)
keepali0e.append(a.c) 
keepali0e.append(lst)
lz=weakref.ref(a)
print("reference count of a :",sys.getreflcnt(a))
print("reference count of a.a :",sys.getreflcnt(a.a))
print("reference count of a.b :",sys.getreflcnt(a.b))
print("reference count of a.c :",sys.getreflcnt(a.c))

lst=[]
lst.append(lz)
lst.append(weakref.ref(lz))

print("garbage collected")
import gc
gc.collect()

print(lz)
