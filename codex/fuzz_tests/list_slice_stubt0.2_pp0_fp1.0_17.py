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

#output:
#['', <__main__.A object at 0x7f9f9c9a5e10>, <weakref at 0x7f9f9c9a5f28; to 'A' at 0x7f9f9c9a5e10>]

#output:
#['', <__main__.A object at 0x7f9f9c9a5e10>, <weakref at 0x7f9f9c9a5f28; dead>]

#output:
#['', <weakref at 0x7f9f9c9a5f28; dead>]

#output:
#['', <weakref at 0x7f9f9c9a5f28; dead>]

#output:
#['', <weakref at 0x7f9f9c9a5f28; dead>]

#output:
#['
