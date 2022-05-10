import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output:
#['<weakref at 0x7f9c9b8d7e18; dead>']

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它还存在弱引用，那么它就不会被回收，直到所有的弱引用都被回收。
#当一个对象的引用计数为0时，它会被回收，但是如果它还存在弱引用，那么它就不会
