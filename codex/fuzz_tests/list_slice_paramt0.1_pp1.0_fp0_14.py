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

#结果：['<__main__.A object at 0x7f9b9c0b7e10>']
#结论：弱引用的回调函数不会被调用，因为弱引用的对象被删除后，弱引用对象也会被删除，所以回调函数不会被调用

#示例2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果：
