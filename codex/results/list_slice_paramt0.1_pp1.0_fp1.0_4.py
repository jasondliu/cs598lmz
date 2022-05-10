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

#结果：['<__main__.A object at 0x0000000003A9B908>']
#结论：弱引用的回调函数不会被调用，因为弱引用的对象还有一个强引用，即a.c=a

#测试2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a.c
del a
print lst

#结果：[]
#结论：弱引用的回调函数会
