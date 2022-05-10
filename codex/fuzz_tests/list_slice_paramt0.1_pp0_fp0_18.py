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
#['<__main__.A object at 0x7f9b9e8f2c50>']
#这个结果说明，当a被删除时，a.c也被删除，因此callback被调用，lst中的元素被删除。

#第二个例子：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst

#结果：
#['<__main__.A object at 0x7f9b9
