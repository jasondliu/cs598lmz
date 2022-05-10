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

#输出：['<__main__.A object at 0x7f7f6d0>']
#结论：弱引用的回调函数不会被调用，因为对象a还有一个强引用，即a.c=a

#例子2：
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print lst

#输出：[]
#结论：弱引用的回调函数会被调用，因为对象a没
