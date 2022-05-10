import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#输出：['<__main__.A object at 0x000002A0D7F8C898>']
#结论：对象a的弱引用被删除，但是对象a本身还存在，因为a.c=a，对象a的引用计数为1，所以对象a不会被回收

#第二个例子
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
a=None
print
