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
#['', <__main__.A object at 0x000002B9B9F2B908>]
#这个结果说明，在循环引用的情况下，gc.collect()并不能回收对象，因为对象的引用计数不为0

#结论：
#1.引用计数为0时，对象会被回收
#2.循环引用的情况下，引用计数不为0，对象不会被回
