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
#['', <__main__.A object at 0x000002B9F7A9E908>]
#这里的结果是因为，在删除a的时候，a的引用计数减少了1，但是a.c还是指向a，所以a的引用计数还是1，所以a不会被回收，所以lst中的a还是存在的。

#第二种情况：
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=
