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

#结果：['<__main__.A object at 0x7f9b8c0f7b90>']
#结论：当对象被删除后，弱引用对象的回调函数会被调用，但是回调函数中的对象还是存在的，只是不能被访问了。

#测试2：
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
print keepali0e[0]()

#
