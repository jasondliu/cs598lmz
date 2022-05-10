import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.b=b
keepalive.append(a)
keepalive.append(b)
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(b,callback))
del a
del b
print(lst)

#[str(), weakref.ref(<__main__.A object at 0x0000000001D2F828>), weakref.ref(<__main__.A object at 0x0000000001D2F7F0>)]
#[str(), weakref.ref(<__main__.A object at 0x0000000001D2F828>), weakref.ref(<__main__.A object at 0x0000000001D2F7F0>)]
#[str(), weakref.ref(<__main__.A object at 0x0000000001D2F828>), weakref.ref(<__main__.A object at 0x0000000001D2F7F0>)]
#[str(), weakref.ref(<__main__.
