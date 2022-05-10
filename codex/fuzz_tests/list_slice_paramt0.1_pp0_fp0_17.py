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

#结果：['a']
#结论：弱引用的回调函数在对象被回收时被调用，回调函数的参数是弱引用对象本身，而不是被引用的对象。

#弱引用的回调函数在对象被回收时被调用，回调函数的参数是弱引用对象本身，而不是被引用的对象。
#弱引用的回调函数在
