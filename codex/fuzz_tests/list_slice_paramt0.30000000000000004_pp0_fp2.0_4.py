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

#结果：['<__main__.A object at 0x000002A6E9E9A8D0>']
#结论：弱引用的回调函数不会被调用，因为弱引用的对象是一个循环引用，所以不会被回收

#实例2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：[]
#结论：弱引用的回调函数
