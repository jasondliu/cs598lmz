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
#['<__main__.A object at 0x0000000003A9D908>']

#结论：
#当一个对象的引用计数为0时，如果该对象的弱引用计数不为0，则该对象不会被回收，
#直到该对象的弱引用计数为0时，该对象才会被回收。

#结论：
#当一个对象的引用计数为0时，如果该对象的弱引
