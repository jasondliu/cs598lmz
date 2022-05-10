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
#['', <__main__.A object at 0x000002C9F9A9E908>]
#这个结果说明，在删除a的时候，a的引用计数为0，但是a的c属性指向a，所以a的引用计数又变成了1，所以a没有被回收。
#这个结果说明，在删除a的时候，a的引用计数为0，但是a的c属性指
