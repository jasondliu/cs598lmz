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

#结果：['', <weakref at 0x0000020B9D9E3D68; to 'A' at 0x0000020B9D9E3C48>]
#结论：当对象a被删除后，a的弱引用依然存在，但是a的弱引用不会被回调函数删除，因为a的弱引用存在于a的弱引用列表中，而a的弱引用列表存在于a中，a的弱引用列表存在于a中，a的弱
