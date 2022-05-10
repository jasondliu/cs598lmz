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

#输出：['<__main__.A object at 0x7f8f9d9b5f10>']
#结论：弱引用的回调函数在对象被回收时被调用，但是不能保证回调函数被调用时对象还存在

#练习2
import weakref
class A(object):pass
def callback(x):print 'callback'
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#输出：['<__main__.A object at 0x7f8f9d9b5f10>']
