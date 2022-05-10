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
#['<__main__.A object at 0x00000000024D7E10>']

#结论：
#当一个对象的弱引用被回调时，它的引用计数会减1，但是不会被销毁。
#当一个对象的引用计数为0时，它会被销毁。
#当一个对象的引用计数为0时，它的弱引用会被回调。
#当一个对象的引用计数为0时，它的弱
