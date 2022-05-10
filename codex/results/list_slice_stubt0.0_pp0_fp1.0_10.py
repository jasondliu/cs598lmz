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
#['', <__main__.A object at 0x000002A8E8E8D908>]
#这里的结果是因为，在删除a的时候，a的引用计数为1，因为lst中还有一个引用，所以a不会被回收，
# 当lst被回收的时候，a的引用计数为0，所以a被回收，但是a中的c还是指向a，所以a不会被回
