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
#[<weakref at 0x000002C8D8C8A948; to 'A' at 0x000002C8D8C8A908>, []]
#这里的结果是因为a.c=a的原因，a.c引用了a，所以a不会被回收，而lst[0]被回收了，所以lst变成了空列表

#练习2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(
