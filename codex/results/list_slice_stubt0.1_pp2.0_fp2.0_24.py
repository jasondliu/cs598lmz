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

#结果：['', <__main__.A object at 0x000002A8F8E9A908>]
#结论：弱引用不会增加对象的引用计数，但是弱引用对象本身会增加引用计数

#练习：
#1.编写一个程序，让它创建一个对象，然后创建一个弱引用指向该对象，最后删除该对象，并打印
