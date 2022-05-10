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

#第一个参数是要弱引用的对象，第二个参数是回调函数，当对象被回收时，回调函数会被调用。
# 回调函数的参数是被回收的对象。
# 回调函数的返回值会被忽略。
# 回调函数会在对象被回收时调用，但不能保证会立即调用。
# 如果回调函数引用了
