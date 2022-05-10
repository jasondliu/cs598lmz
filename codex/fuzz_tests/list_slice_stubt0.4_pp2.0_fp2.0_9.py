import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=callback
del lst
gc.collect()
print(keepalive)

#对象的引用计数，不会因为引用计数为0就被回收
#引用计数只会在对象被创建和销毁时被改变，在对象被创建时，引用计数为1，在对象被销毁时，引用计数为0
#引用计数的缺点：循环引用，引用计数无法回
