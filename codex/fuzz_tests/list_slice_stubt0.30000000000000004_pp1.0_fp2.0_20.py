import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
del keepalive
print(lst)

#结果：['', <__main__.A object at 0x7f2f1b8e6f98>, <weakref at 0x7f2f1b8e6f28; to 'A' at 0x7f2f1b8e6f98>]
#结论：weakref.ref(a,callback)这个弱引用对象，只要a这个对象没有被回收，那么这个弱引用对象就不会被回收
#      只有当a这个对象被回收的时候
