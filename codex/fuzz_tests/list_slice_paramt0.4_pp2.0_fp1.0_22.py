import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a

import gc
gc.collect()
print lst

#[str(), <__main__.A object at 0x00000000020C5B38>]

#这里的A对象是弱引用的，当引用计数为0时，弱引用对象会被回收，这时会调用callback函数，在callback函数中删除lst中的对象，这时lst中的对象就是弱引用对象，所以弱引用对象会被回收，这时lst中的对象就是None，所以最后打印
