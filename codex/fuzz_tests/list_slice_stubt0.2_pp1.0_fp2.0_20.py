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
print(keepalive)

#结果：
#[str(), <weakref at 0x000002A8C7E9D948; to 'A' at 0x000002A8C7E9D828>]
#[<__main__.A object at 0x000002A8C7E9D828>]

#结论：
#当对象被回收时，会调用callback函数，并将lst中的弱引用删除。
#但是由于keepalive中的强引用，对象并没有被回收。
#所以lst中的弱引用并没有被
