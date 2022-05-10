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

# 可以看到，当循环引用的对象被删除后，会调用回调函数。
# 在实际的应用中，会有很多这样的循环引用，如果不能及时被回收，会导致内存泄漏。
# 如果没有回调函数，可以使用gc.collect()来强制回收，但是这种方式不够精确，gc模块提供了一个
