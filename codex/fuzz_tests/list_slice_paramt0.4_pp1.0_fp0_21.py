import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
print lst

#输出：
['1']

#结论：
#循环引用时，只要有一个对象被回收，另一个对象也会被回收。
#除非对象有__del__方法，否则不会调用回调函数。

#疑问：
#为什么没有调用回调函数？
#为什么没有输出？

#答案：
#因为在python
