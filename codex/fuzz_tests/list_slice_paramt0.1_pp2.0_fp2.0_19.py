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
#['<__main__.A object at 0x7f7b7c0f0a90>']

#结论：
#当一个对象的弱引用被回调函数调用时，该对象的弱引用被删除，但是该对象本身并不会被删除。
#这是因为弱引用只是对象的一个弱引用，并不是对象的唯一引用。
#当对象的弱引用被删除时，该对象的引用计
