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

#结果：['<__main__.A object at 0x0000000003D8D898>']
#结论：当一个对象的弱引用被删除时，调用回调函数，但是回调函数中的对象还是存在的，只是弱引用被删除了

#示例2
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

#结果：callback
#结论：
