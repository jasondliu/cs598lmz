import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print(lst)

#结果是：
#['\x00']
#这是因为，当a被删除时，a.c的弱引用被删除，而a.c的弱引用又删除了a的弱引用，
#所以a的弱引用没有被删除，所以lst中的第一个元素没有被删除。

#如果把a.c的弱引用删除，则结果是：
#[]
#这是因为，当a
