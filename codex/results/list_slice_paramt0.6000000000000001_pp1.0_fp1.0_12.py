import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a,callback))
del a
del lst
for i in range(10):
    try:
        print(keepali0e[0](),keepali0e[1]())
    except:
        pass
    else:
        break
    import gc
    gc.collect()
    time.sleep(1)

#模拟命名空间
import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a,callback))
del a
del lst
for i in range(10):
    try:
        print(keepali0e[0](),keepali0e[1]())
    except:
        pass
    else:
        break
    import gc
    gc.collect()
   
