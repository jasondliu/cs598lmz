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

#结果：['', <__main__.A object at 0x0000000003B8B828>]
#结论：当对象的引用计数为0时，调用__del__方法，但是当对象的引用计数不为0时，不会调用__del__方法
#结论：当对象的引用计数为0时，调用__del__方法，但是当对象的引用计数不为0时，不会调用__del__方法
#结
