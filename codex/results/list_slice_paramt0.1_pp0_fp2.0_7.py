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
#['<__main__.A object at 0x7f9c9f9d5c50>']

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收，但是如果它还存在循环引用，那么它就不会被回收。
#当一个对象的引用计数为0时，它会被垃圾回收，但是如果它还存在循环引用，那么它就不会被回
