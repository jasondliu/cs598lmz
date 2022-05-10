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
#['<__main__.A object at 0x7f9d9a8e7a90>']

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它有一个弱引用，它就不会被回收，因为弱引用不会增加引用计数。
#当一个对象的引用计数为0时，它会被回收，但是如果它有一个弱引用，它就不会被
