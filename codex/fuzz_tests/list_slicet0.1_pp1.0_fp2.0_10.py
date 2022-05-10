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
print(keepali0e)

#结果：
#[<weakref at 0x000002A9A9C7B948; to 'A' at 0x000002A9A9C7B898>, ['']]
#结论：
#当对象被回收时，会调用回调函数，并且回调函数会改变列表的值，所以列表的值会变成['']

#第二种情况：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while
