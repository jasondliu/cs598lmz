import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print(lst)

#结果：
#['', <__main__.A object at 0x000002B8A8F8C908>]

#结论：
#在python中，对象的引用计数只有在对象被创建时才会被计数，而在对象被销毁时不会被计数。
#因此，在对象被销毁时，对象的引用计数不会减少，这就导致了循环引用的问题。
