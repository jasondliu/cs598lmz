import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
import gc
gc.collect()
print(lst)
#['<weakref at 0x10cff5a68; to 'A' at 0x10cff5b70>']
#因为A对象本身是弱引用，但是A对象中的c属性是对A对象本身的强引用，
# 因此当A对象被回收时，A对象中的c属性指向的A对象也不会被回收，因此lst中只剩下一个弱引用。
