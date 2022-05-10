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

#结果：[str(), <weakref at 0x000002B6A0A6D7C8; to 'A' at 0x000002B6A0A6D898>]
#结论：当删除a的时候，a的引用计数减少，但是由于a.c=a，所以a的引用计数不为0，所以a不会被回收，
#所以lst[1]不会被回收，所以lst[0]不会被回收，所以lst[0]不会被回
