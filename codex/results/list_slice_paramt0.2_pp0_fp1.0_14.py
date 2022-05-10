import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：['str()']
#结论：当弱引用的对象被回收时，会调用回调函数，并将弱引用对象作为参数传入回调函数，
#回调函数的返回值被忽略，回调函数可以抛出异常，但是不会被捕获。

#例子2：
import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e
