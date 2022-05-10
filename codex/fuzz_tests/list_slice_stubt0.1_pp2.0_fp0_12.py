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
print lst
print keepalive

#[str(), <weakref at 0x0000000003A8B948; to 'A' at 0x0000000003A8B908>]
#[<__main__.A object at 0x0000000003A8B908>]

#这里的lst[0]是一个str()，lst[1]是一个弱引用，指向a，a.c指向a，所以a不会被回收，
#当a被回收时，lst[1]会被回调，删除lst[0]，这样lst[0]就不会被回收，
#所以
