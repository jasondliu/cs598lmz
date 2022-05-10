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
#['<__main__.A object at 0x0000000003A8B908>']

#结论：
#当一个对象的引用计数为0时，会调用__del__方法，但是如果这个对象还有弱引用，那么这个对象不会被回收，
#直到所有的弱引用都被回收，这个对象才会被回收，并且调用__del__方法。

#结论：
#当一个对
