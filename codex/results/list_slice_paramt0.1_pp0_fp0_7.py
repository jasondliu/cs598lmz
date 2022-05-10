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
#['\x00']

#结论：
#当一个对象的弱引用被删除时，调用回调函数，回调函数的参数是弱引用对象的引用，
#如果弱引用对象的引用是None，则说明弱引用对象已经被回收，否则说明弱引用对象还存在。

#结论：
#当一个对象的弱引用被删除时
