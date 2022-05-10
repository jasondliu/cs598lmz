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

#结果：
#[str(), <weakref at 0x000002A9D0D8C948; to 'A' at 0x000002A9D0D8C908>]
#[str()]

#结论：
#当一个对象的引用计数为0时，会调用__del__方法，但是如果这个对象的引用计数为0，但是还有弱引用指向它，那么这个对象就不会被回收，
#直到这个对象的弱
