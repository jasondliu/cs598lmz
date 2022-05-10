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

#结果：
#[str(), <weakref at 0x000002A9E6F9A948; to 'A' at 0x000002A9E6F9A898>]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
