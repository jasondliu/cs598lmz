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
#['<__main__.A object at 0x0000000003A8F9B0>']

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收器回收，但是如果它有一个弱引用，那么它就不会被回收，
#直到弱引用也被回收。

#弱引用的作用：
#1.防止内存泄漏
#2.实现缓存
#3.实现代理

#弱引
