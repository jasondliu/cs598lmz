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

#结果：
#['', <__main__.A object at 0x000002A6F7F6E908>]
#[<__main__.A object at 0x000002A6F7F6E908>]

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它的引用计数为0，但是它的引用计数为0，但是它的引用计数为0，但是它的引用计数为0，但是它的引
