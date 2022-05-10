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

#[str(), <weakref at 0x00000000026A2E88; to 'A' at 0x00000000026A2F28>]
#[<__main__.A object at 0x00000000026A2F28>]

#第二次
#[str()]
#[<__main__.A object at 0x00000000026A2F28>]

#第三次
#[str()]
#[]

#第四次
#[str()]
#[]

#第五次
#[str()]
#[]

#第六次
#[str()]
#[]

#第七次
#[str()]
#[]

#第八次
#[str()]
#[]

#第
