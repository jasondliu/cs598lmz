import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(lst,callback))
del lst
try:
    import gc
    gc.collect()
except:
    pass
if lst or not keepali0e:print("Failed")
else:print("OK")
