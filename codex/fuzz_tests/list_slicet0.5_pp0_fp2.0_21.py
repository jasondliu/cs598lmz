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

#下面的代码是一个循环引用的例子，结果是不会被回收的，因为没有调用gc.collect()
class A(object):pass
a=A()
a.c=a
del a

#下面的代码是一个循环引用的例子，结果是会被回收的，因为调用了gc.collect()
import gc
class A(object):pass
a=A()
a.c=a
del a
gc.collect()

#下面的代码是一个弱引用的例子，结果是会被回收的
import weakref
class A(object):pass
