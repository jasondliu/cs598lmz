import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(lst)
del a
del keepali0e
import gc
gc.collect()
lst

print("pass" if (lst==[]) else "fail")
