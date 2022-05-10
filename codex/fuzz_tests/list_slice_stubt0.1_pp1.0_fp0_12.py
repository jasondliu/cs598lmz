import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

#结果：
#['', <__main__.A object at 0x000002A9D9D9F908>, <weakref at 0x000002A9D9D9F948; to 'A' at 0x000002A9D9D9F908>]
#这里的结果是因为a.c=a，所以a的引用计数为2，所以a不会被回收，所以lst[2]不会被回收，所以lst[1]不会被回收，所以lst[0]不会被回收

#结
