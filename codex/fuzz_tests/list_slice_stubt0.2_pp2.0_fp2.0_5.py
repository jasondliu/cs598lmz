import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
print(lst)
del a
print(lst)
lst.append(weakref.ref(lst,callback))
print(lst)
del lst
print(lst)

#[str(), <__main__.A object at 0x7f5f5c5e6b38>]
#[str(), <__main__.A object at 0x7f5f5c5e6b38>]
#[str(), <__main__.A object at 0x7f5f5c5e6b38>, <weakref at 0x7f5f5c5e6c18; dead>]
#[str(), <__main__.A object at 0x7f5f5c5e6b38>, <weakref at 0x7f5f5c5e6c18; dead>]

#结论：
#1. 弱引用的回调函数是在被引
