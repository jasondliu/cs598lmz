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
#['', <__main__.A object at 0x7f8e6c5c5b38>]
#[<__main__.A object at 0x7f8e6c5c5b38>]

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它的某个属性的值是它自己，那么它的引用计数就不会为0，
#也就不会被回收，这就是循环引
