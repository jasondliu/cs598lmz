import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print(lst)

#结果：
#['']

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它的__del__方法中有引用它的对象，那么它的引用计数就不为0，不会被回收，
#这样就会出现循环引用，导致内存泄漏。
#解决方法：
#1.使用弱引用，弱引
