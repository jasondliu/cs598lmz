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

#结果为：['<__main__.A object at 0x00000000020B6C18>']
#结论：当引用计数为0时，会调用回调函数，并将弱引用对象从lst中删除，但是弱引用对象本身还是存在的

#练习2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果为：[]
#结论：当引用
