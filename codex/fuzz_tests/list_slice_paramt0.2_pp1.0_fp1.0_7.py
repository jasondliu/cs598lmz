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

#输出：['<__main__.A object at 0x000002A6E8E6C1D0>']
#结论：对象a的弱引用被删除后，回调函数被调用，删除了lst的第一个元素

#示例2
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

#输出：['<__main__.A object at 0x000002A6E8E6C1D0>']
#结论
