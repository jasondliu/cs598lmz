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
del keepalive[0]
print(lst)
print(lst[0]())
print(lst)

#[str(), <weakref at 0x0000020B9E9E9A98; to 'A' at 0x0000020B9E9E9B00>]
#<__main__.A object at 0x0000020B9E9E9B00>
#[<weakref at 0x0000020B9E9E9A98; dead>]

#第一个str()是列表中的第一个元素，第二个是weakref.ref(a,callback)，
#当a被回收时，会调用callback，callback中删除了列表中的第一个元素，
#
