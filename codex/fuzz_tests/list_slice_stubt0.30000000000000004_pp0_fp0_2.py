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
lst[0]=callback
lst[0]()
print(lst)
print(keepalive)

#结果是：
#[<__main__.A object at 0x000002B5B7E0F208>]
#[<__main__.A object at 0x000002B5B7E0F208>]

#结论：
#当一个对象的引用计数为0时，就会被回收，但是如果这个对象还有引用，就不会被回收。
#当一个对象的引用计数为0时，会触发__del__方法，但
