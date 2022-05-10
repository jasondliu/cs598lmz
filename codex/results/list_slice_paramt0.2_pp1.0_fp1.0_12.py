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
print(lst)
print(keepali0e)

#结果：
#['', <__main__.A object at 0x000002A3C8F8E908>]
#[<weakref at 0x000002A3C8F8E948; to 'A' at 0x000002A3C8F8E908>]

#结论：
#1.当一个对象的引用计数为0时，该对象会被回收，但是如果该对象的引用计数为0，但是还存在弱引用，则该对象不会被回收。
#2.当一个对象
