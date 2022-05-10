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
#['', <__main__.A object at 0x000002A8E8F8D908>]
#这里的结果是因为a.c=a，所以a的引用计数为2，所以a不会被回收，所以lst中的a不会被回收

#结论：
#1.弱引用的对象在没有其他强引用的情况下会被回收
#2.弱引用的对象在有其他强引用的情况下不
