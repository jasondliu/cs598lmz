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
#['<__main__.A object at 0x7f8d6c0e7b90>']

#结论：
#当一个对象的弱引用被删除时，回调函数被调用。
#当一个对象的弱引用被删除时，回调函数被调用。
#当一个对象的弱引用被删除时，回调函数被调用。
#当一个对象的弱引用被删除时，回调函数被
