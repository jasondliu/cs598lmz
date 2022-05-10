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
print keepalive

#[str(), <weakref at 0x00000000028E8C48; to 'A' at 0x00000000028E8C88>]
#[<__main__.A object at 0x00000000028E8C88>]

#第二次运行
#[str()]
#[<__main__.A object at 0x00000000028E8C88>]

#第三次运行
#[str()]
#[<__main__.A object at 0x00000000028E8C88>]

#第四次运行
#[str()]
#[<__main__.A object at 0x00000000028E8C88>]

#第五次运行
#[str()]
#[<__main__.A object at 0x00000000028E8
