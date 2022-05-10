import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

# 弱引用的另一个用途是实现缓存。
# 当一个对象被弱引用引用时，它不会增加引用计数。
# 因此，当引用计数为0时，该对象会被垃圾回收机制回收。
# 如果一个对象被弱引用引用，并且没有其他强引用指向它，那么它会被回收。
# 如果一个对象只被
