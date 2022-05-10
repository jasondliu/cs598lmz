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
#['<__main__.A object at 0x7f9a9a8a2c50>']

#结论：
#当一个对象的引用计数为0时，如果这个对象的弱引用计数不为0，则不会被回收。
#当一个对象的引用计数为0时，如果这个对象的弱引用计数为0，则会被回收。
#当一个对象的引用计数不为0时，不管这个对
