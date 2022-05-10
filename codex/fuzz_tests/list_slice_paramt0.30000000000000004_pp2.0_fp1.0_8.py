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

#结果：['a']

#结论：当循环引用中有一个对象是弱引用时，那么这个弱引用对象会被回收，而不是等待循环引用中的其他对象被回收。

#结论：弱引用对象在回收时，会调用回调函数。
