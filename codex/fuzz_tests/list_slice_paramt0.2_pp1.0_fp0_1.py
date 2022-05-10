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
#['<__main__.A object at 0x7f9a9c6a8b90>']

#结论：
#当一个对象的引用计数为0时，它会被销毁，但是在销毁之前，会检查该对象是否有弱引用，如果有，则会调用回调函数。
#如果回调函数中使用了该对象，则会导致该对象的引用计数变为1，从而不会
