import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

# 弱引用的回调函数
# 弱引用的回调函数会在对象被回收时被调用，回调函数的参数是弱引用对象本身，回调函数可以通过该参数获取到被回收的对象。
# 回调函数的返回值会被忽略。
# 回调函数的调用时机是不确定的，可能是在对
