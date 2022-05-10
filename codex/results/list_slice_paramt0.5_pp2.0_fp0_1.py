import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print(lst)

# 弱引用可以被垃圾回收器回收，不可以被垃圾回收器回收的对象，可以被弱引用
# 弱引用的回调函数
# 弱引用的回调函数，会在对象被垃圾回收器回收前调用
# 在回调函数中，可以获取被回收的对象，或者获取被回收对象的引用
#
