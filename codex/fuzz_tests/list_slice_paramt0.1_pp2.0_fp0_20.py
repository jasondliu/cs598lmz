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
#['<__main__.A object at 0x0000000003E9E908>']

#结论：
#当一个对象的弱引用被回调函数调用时，该对象的弱引用被删除，但是该对象本身并不会被删除，
#因为该对象还有一个强引用，即自己的引用，所以该对象不会被垃圾回收器回收。

#结论：
#当一个
