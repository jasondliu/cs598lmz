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
#['<__main__.A object at 0x0000000003B9D908>']

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它的弱引用计数不为0，它就不会被回收，
#这样就会导致内存泄漏，所以在使用弱引用时要注意这个问题。

#结论：
#当一个对象的引用计数为0时，它
