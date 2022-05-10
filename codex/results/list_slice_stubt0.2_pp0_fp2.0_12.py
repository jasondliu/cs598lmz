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
#[str(), <weakref at 0x000002A9E9E9D948; to 'A' at 0x000002A9E9E9D898>]

#结论：
#weakref.ref(a,callback)中的callback函数在a被回收时被调用，
#但是callback函数中的del lst[0]并不会被调用，
#因为lst[0]是一个str()对象，不会被回收，
#所以lst[0]不会被删除，lst[1]也不会被删
