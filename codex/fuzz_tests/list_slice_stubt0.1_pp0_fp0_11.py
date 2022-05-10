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
#['', <__main__.A object at 0x000002A9A9F9C908>]
#这里的结果是因为a.c=a，所以a的引用计数为2，所以不会被回收

#结论：
#弱引用的目的是为了避免循环引用，当引用计数为0时，就会被回收，所以弱引用不会增加引用计数

#弱引用的使用场景
