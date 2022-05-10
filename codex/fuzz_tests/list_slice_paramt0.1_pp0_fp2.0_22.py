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

#结果：
#['<__main__.A object at 0x7f8b9d6b9f28>']

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收，但是如果它的引用计数为0，但是它的弱引用计数不为0，那么它就不会被垃圾回收，
#直到它的弱引用计数为0时，它才会被垃圾回收。

#结论：
#当一
