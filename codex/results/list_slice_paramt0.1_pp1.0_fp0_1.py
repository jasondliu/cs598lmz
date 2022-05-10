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
#['<__main__.A object at 0x7f7c8c0b5f50>']
#这个结果说明，当a被删除时，a.c的弱引用被删除，但是a.c的弱引用指向的对象a还存在，所以a.c的弱引用没有被删除，所以lst中的元素没有被删除。

#第二个例子：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
