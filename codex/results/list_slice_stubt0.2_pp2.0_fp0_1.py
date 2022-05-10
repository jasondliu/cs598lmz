import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)
print(keepalive)

#结果：
#['', <__main__.A object at 0x000001E7B0D8E908>, <weakref at 0x000001E7B0D8E8C8; to 'A' at 0x000001E7B0D8E908>]
#[<__main__.A object at 0x000001E7B0D8E908>]

#结论：
#当弱引用所指向的对象被回收时，回调函数会被调用，回调函数的参数是弱引用对象本身，而
