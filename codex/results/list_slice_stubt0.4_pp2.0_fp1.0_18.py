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
del keepalive
gc.collect()
print lst

#输出：
#['', <__main__.A object at 0x0000022E8B7FDBE0>]
