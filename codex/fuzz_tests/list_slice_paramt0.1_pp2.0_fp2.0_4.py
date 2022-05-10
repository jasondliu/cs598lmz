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
#['<__main__.A object at 0x7f8e9b9f3b90>']
#这个结果说明，当a被删除时，a.c的引用计数为1，所以a.c不会被删除，所以lst中的弱引用不会被删除，所以lst中的字符串不会被删除。

#第二个例子：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.
