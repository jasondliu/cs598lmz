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

#第二种方法
import gc
gc.disable()
lst=[]
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#第三种方法
import gc
gc.disable()
lst=[]
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
gc.enable()
gc.collect()

#第四种方法
import gc
gc.disable()
lst=[]
class A(object):pass
def callback(x):del
