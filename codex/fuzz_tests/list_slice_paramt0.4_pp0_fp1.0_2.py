import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(keepali0e[0])
del a
print lst

#结果为['', <weakref at 0x7f8d8b9c9a78; to 'A' at 0x7f8d8b9c9b10>]
#因为a.c=a，a的引用计数为2，所以a不会被回收，只有当lst中的引用计数为0时，a才会被回收，
#所以callback函数只会在del lst[0]时被调用。

#3.2 简单的弱引用
#弱引用只是一种简单的引用，不会增加
