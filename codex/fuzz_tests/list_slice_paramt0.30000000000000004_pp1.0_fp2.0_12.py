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
#['A']

#结论：
#当一个对象的引用计数为0时，它就会被垃圾回收器回收，但是这个对象的弱引用还是可以被访问的。
#当一个对象的弱引用计数为0时，它就会被垃圾回收器回收，这个对象的弱引用也不能被访问了。
