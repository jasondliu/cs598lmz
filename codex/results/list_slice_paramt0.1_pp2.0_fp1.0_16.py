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
#['<__main__.A object at 0x7f8d8c0a8b90>']

#结论：
#当一个对象的弱引用被回调函数删除时，该对象的引用计数会减1，当引用计数为0时，该对象会被回收。
#当一个对象的弱引用被回调函数删除时，该对象的引用计数会减1，当引用计数为0时，该对
