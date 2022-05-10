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
#['<weakref at 0x7f7f8c0b8c78; to 'A' at 0x7f7f8c0b8c50>']

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收器回收，但是如果它有一个循环引用，那么它就不会被回收，
#因为它的引用计数不为0，这样就会导致内存泄露。
#weakref模块可以解决这个问题
