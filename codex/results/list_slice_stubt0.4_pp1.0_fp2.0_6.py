import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
keepalive.append(a)
del a
lst[0]=weakref.ref(lst,callback)
del lst
print(keepalive)

#[<__main__.A object at 0x10e6d2e10>]

# 这个例子说明，当弱引用的对象被回收时，这个弱引用对象会被自动删除。
# 当弱引用对象被删除时，会调用回调函数，回调函数的参数是弱引用对象本身。
# 回调函数可以用来删除弱引
