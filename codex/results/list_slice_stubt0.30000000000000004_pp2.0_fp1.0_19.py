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
print(lst)
del a
print(lst)
del keepalive
print(lst)

#结果：
#['', <__main__.A object at 0x000002B2B8F0C320>, <weakref at 0x000002B2B8F0C2F0; to 'A' at 0x000002B2B8F0C320>]
#['', <__main__.A object at 0x000002B2B8F0C320>, <weakref at 0x000002B2B8F0C2F0; dead>]
#['', <__main__.A object at 0x000002B2B8F0C320>, <weakref at 0x000002B2B8F0C2F0; dead>]

#结论：
#1.弱引用的回调函
