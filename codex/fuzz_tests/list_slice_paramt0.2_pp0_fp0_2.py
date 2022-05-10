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
#['<__main__.A object at 0x0000000003A5A5F8>']

#结论：
#当对象的引用计数为0时，会调用回调函数，但是回调函数中的对象仍然存在，因为回调函数中的对象是弱引用，不会影响对象的引用计数，所以对象不会被回收。

#结论2：
#当对象的引用计数为0时，会
