import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#结果：
#['<__main__.A object at 0x000002B0A9A9E7F0>']
#[]

#结论：
#当一个对象的引用计数变为0时，它会被垃圾回收器回收，但是，如果它还存在弱引用，那么它不会被立即回收，而是等待垃圾回收器的下一次扫描时再回收。
#弱引用的一个特点是它的回调
