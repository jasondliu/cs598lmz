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
#['<__main__.A object at 0x7f8b5c0d4f50>']
#这个结果说明，当a被删除时，a.c的引用计数减1，但是a.c还是存在的，因为a.c的引用计数不为0，所以a.c不会被回收，所以lst中的元素不会被删除

#第二个例子：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a

