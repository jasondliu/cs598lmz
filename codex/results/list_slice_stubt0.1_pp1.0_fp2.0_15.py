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
#['', <__main__.A object at 0x000002A8F5D9E9E8>, <weakref at 0x000002A8F5D9E948; to 'A' at 0x000002A8F5D9E9E8>]
#[<__main__.A object at 0x000002A8F5D9E9E8>]

#结论：
#1.lst[0]是一个空字符串，lst[1]是一个A类的实例，lst[2]是一个弱引用，引用的是lst[1]
#2.lst[1]的c属
