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

#[str(), <weakref at 0x7f7c4d2e8c68; to 'A' at 0x7f7c4d2e8c90>]
#[<__main__.A object at 0x7f7c4d2e8c90>]

#这里的keepalive是一个列表，列表中的元素是一个类的实例，实例中的c属性是实例本身，
#这样就形成了一个循环引用，这个实例就不会被回收，
#lst是一个列表，列表中的
