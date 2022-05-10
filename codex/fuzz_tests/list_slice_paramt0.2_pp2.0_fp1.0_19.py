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
#['<__main__.A object at 0x7f9f9f8d7b90>']
#结论：
#当对象被删除时，会调用回调函数，回调函数的参数是弱引用对象，此时弱引用对象的值是None
#回调函数的参数是弱引用对象，而不是原始对象

#例子2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a

