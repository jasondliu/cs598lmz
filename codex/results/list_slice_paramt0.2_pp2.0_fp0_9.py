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

#输出：['<__main__.A object at 0x7f0c4f9b9c50>']
#结论：当一个对象的引用计数为0时，如果该对象的弱引用计数不为0，则该对象不会被回收

#示例2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#输出：[]
#结论：当一个对象的引用
