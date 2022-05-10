import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果：
#['<__main__.A object at 0x7f7f8c0f4b90>']
#这个结果说明，当a被删除时，a.c的弱引用被删除，但是a.c的强引用还在，所以a.c不会被删除，所以a.c的弱引用不会被删除，所以a的弱引用不会被删除，所以a不会被删除，所以lst不会被删除。

#下面是一个比较
