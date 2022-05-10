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
del keepali0e
print(lst)

#结果：
#['a']
#[]

#结论：
#当对象被删除时，回调函数会被调用，但是回调函数中的对象不会被删除，因为回调函数中的对象是弱引用，不会影响对象的生命周期

#结论：
#当对象被删除时，回调函数会被调用，但是回调函数中的
