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

#结果：['\x00']
#结论：当对象被回收时，会调用回调函数，回调函数中的参数是被回收的对象

#示例2：
import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：<__main__.A object at 0x7f6f9c0b7c50>
#结论：当对象被回收时，会
