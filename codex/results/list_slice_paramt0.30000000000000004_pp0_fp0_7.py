import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
print keepali0e

#结果：
#['a']
#[<weakref at 0x01D8E7F0; dead>]

#结论：
#在删除对象a时，a.c=a，导致a不能被回收，因为a.c指向a，a.c指向a，a.c.c指向a.c，a.c.c.c指向a.c.c，
#以此类推，a.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c
