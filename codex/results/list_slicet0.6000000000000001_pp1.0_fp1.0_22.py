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

#第二个方法，利用了系统的垃圾回收机制
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
gc.collect()
while lst:keepali0e.append(lst[:])

#第三个方法，把循环引用放到线程里面，线程结束，线程里面的变量就会被回收
import gc
import weakref
import threading
import time
class A(object):pass
def callback(x):del l
