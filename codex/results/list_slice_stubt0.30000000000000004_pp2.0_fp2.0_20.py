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
print lst

#程序运行结果：
#[str(), <weakref at 0x00000000029B1D48; to 'A' at 0x00000000029B1D30>]
#程序解释：
#程序中，a.c=a，这样a就有了一个引用，虽然a被删除了，但是a还有一个引用，所以a不会被回收，
#lst[0]被回收了，但是lst[1]还存在，所以lst[1]还是存在的，所
