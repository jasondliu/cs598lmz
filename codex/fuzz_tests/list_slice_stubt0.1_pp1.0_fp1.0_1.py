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

#结果：['', <__main__.A object at 0x000002B8F9E9B908>]
#结论：
#1.弱引用的对象在垃圾回收时会被回收
#2.弱引用的对象在垃圾回收时会调用回调函数
#3.弱引用的对象在垃圾回收时会调用回调函数，回调函数可以删除弱引用的对象
#4.弱引用的
