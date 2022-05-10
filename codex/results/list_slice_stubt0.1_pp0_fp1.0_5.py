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
print(keepalive)

#['']
#[<__main__.A object at 0x000002A8D8E9F9B0>]

#结论：
#1.当一个对象的引用计数为0时，它会被垃圾回收，但是如果它的引用计数不为0，它就不会被垃圾回收
#2.当一个对象的引用计数为0时，它的__del__方法会被调用，但是如果它的引用计数
