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

#结果：['<__main__.A object at 0x7f8b4d0b7d50>']
#这个结果说明，当一个对象的引用计数为0时，它的弱引用计数也为0，因此回调函数被调用。
#但是，如果一个对象的引用计数不为0，它的弱引用计数也不为0，回调函数不会被调用。

#结论：
#1.弱引用计数为0时，
