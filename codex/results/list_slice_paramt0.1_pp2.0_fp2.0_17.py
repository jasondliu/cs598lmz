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
#['<__main__.A object at 0x0000000003B8C908>']

#结论：
#当一个对象的弱引用被回调函数调用时，该对象的引用计数为0，但是该对象的内存并没有被回收，
#因为该对象的弱引用对象还存在，所以该对象的内存不会被回收。

#结论：
#当一个对象的弱引用被回调
