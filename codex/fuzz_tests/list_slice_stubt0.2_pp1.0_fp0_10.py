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
print(keepalive)

#结果：
#['']
#[<__main__.A object at 0x000002C9E9D8B9B0>]

#结论：
#当引用计数为0时，会调用回调函数，但是不会调用__del__方法

#结论2：
#当引用计数为0时，会调用回调函数，但是不会调用__del__方法
#当引用计数为0时，会调用回调
