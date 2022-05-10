import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#结果：
#[str(), <weakref at 0x000002A2E7E8D948; to 'A' at 0x000002A2E7E8D898>]
#[str()]
