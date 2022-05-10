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
#['<__main__.A object at 0x7f8e8c0d5e10>']

#结论：
#当一个对象的弱引用被删除时，回调函数被调用，但是回调函数中的对象还是存在的，
#因为回调函数中的对象是一个强引用，所以回调函数中的对象不会被回收。

#结论：
#当一个对象的弱引用被删除时，
