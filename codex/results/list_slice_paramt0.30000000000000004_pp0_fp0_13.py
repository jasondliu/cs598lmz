import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print lst
print keepali0e

#['']
#[<weakref at 0x00B9B7C8; dead>
#
#Process finished with exit code 0
