import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(a)
lst.append(a)
del a
gc.collect()
print(lst)
print(keepali0e)

#[str(), <__main__.A object at 0x7f9f8d8f7b50>]
#[<__main__.A object at 0x7f9f8d8f7b50>]
