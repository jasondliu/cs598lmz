import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print keepali0e

#结果：
#[<weakref at 0x7f8c9c0e7d88; to 'A' at 0x7f8c9c0e7e10>, ['']]
#[<weakref at 0x7f8c9c0e7d88; dead>, ['']]
#[<weakref at 0x7f8c9c0e7d88; dead>, []]
#[]

#结论：
#1.当a被删除时，a.c引用a，a不会被回收
#2.当a.c被删除时，a被回收，callback被调用，lst[0]被删除
#3.当lst[0]被删除时，lst
