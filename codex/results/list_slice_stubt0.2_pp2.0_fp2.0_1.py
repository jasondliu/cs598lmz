import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive.append(a)
del a
lst.append(weakref.ref(lst,callback))
del lst
print(keepalive)

#结果：
#[<__main__.A object at 0x000002B5C6D8D898>]
#这个结果说明，当lst被删除时，lst[0]也被删除了，但是lst[1]还存在，因为lst[1]是一个弱引用，不会增加对象的引用计数，所以lst[1]不会被删除，但是lst[1]的回调函数被
