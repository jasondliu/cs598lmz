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
#['', <__main__.A object at 0x000002A8F8C8C2E8>]
#这个结果说明，在循环引用的情况下，弱引用也不会被回收，因为弱引用不会增加引用计数，所以不会影响循环引用的回收。
#这个结果也说明，弱引用不会影响引用计数，所以不会影响循环
