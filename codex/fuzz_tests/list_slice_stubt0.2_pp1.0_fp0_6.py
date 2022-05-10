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

#[str(), <weakref at 0x000002A9F9D8E8C8; to 'A' at 0x000002A9F9D8E848>]
#[<__main__.A object at 0x000002A9F9D8E848>]

#这里的keepalive是一个列表，里面有一个A类的实例，这个实例的c属性指向自己，
#这样就形成了一个循环引用，这个循环引用会导致A实例不会被回收，
#
