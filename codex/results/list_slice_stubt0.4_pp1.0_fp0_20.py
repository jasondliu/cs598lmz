import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
keepali0e.append(callback)
weakref.ref(a,callback)
del a
del lst
del keepali0e
del callback
gc.collect()

#3、利用weakref.ref()创建弱引用，并且创建一个弱引用列表，然后删除弱引用列表中的弱引用，
#最后进行垃圾回收
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
keepali0e.append(callback)
weakref.ref(a
