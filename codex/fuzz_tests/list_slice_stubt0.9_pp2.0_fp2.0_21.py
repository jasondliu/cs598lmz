import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del keepalive[0]
keepalive=[]
weakref.ref(4,callback)
del a;a=A()
a.c=lst
a.b=a
a.a=a
keepalive.append(a)
del keepalive[0]
keepalive=[]
import gc;gc.collect()
del lst[0]  #if no collector is setup,the segmentation fault is here
print("end")
