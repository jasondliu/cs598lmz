import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#结果：
#['str()']
#[]

#结论：
#弱引用的对象，只要对象被回收，就会调用回调函数，回调函数的参数是弱引用的对象，而不是被回收的对象。
#弱引用的对象，只要对象被回收，就会调用回调函数，回调函数的参数是弱引用的对象，而不是被
