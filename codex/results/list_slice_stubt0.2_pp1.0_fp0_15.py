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
#[str(), <weakref at 0x000002B8A8A9D948; to 'A' at 0x000002B8A8A9D908>]
#[<__main__.A object at 0x000002B8A8A9D908>]

#结论：
#当对象a被删除时，会调用callback函数，删除lst中的第一个元素，
#但是由于a中的c属性指向a本身，所以a不会被回收，所以lst中的第
