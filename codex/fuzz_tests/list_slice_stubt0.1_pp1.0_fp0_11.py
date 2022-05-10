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

#结果：['', <weakref at 0x000002A4D4E8F848; to 'A' at 0x000002A4D4E8F7F0>]
#结论：当对象被删除后，其弱引用会被自动删除

#练习2：
#结果：['', <weakref at 0x000002A4D4E8F848; to 'A' at 0x000002A4D4E8F7F0>]
#结论：当对象被删除后，其弱引用会被自动删
