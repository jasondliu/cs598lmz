import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a.c,callback)
del a
del keepalive
print lst

#Output:
#['<weakref at 0x0B2D3F30; to 'A' at 0x0B2D3C60>']

#The weak reference is still there, but the callback is not called.

#If the callback is called, the list is empty.

#Output:
#[]

#The callback is called when the weak reference is collected.

#Output:
#[]

#This is the expected behavior. The callback is called if the weak reference is collected.

#The weak reference is not collected if the callback is not called.

#Output:
#['<weakref at 0x0B2D3F30; to 'A' at 0x0B2D3C60>']

#The weak reference is not collected if the callback is not called.

#Output:
#['<weakref at 0x0B2D3F30; to 'A' at 0x0B
