import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
del a
print(lst)

# 弱引用
# 弱引用是一种特殊的引用，它的引用计数不会增加对象的引用计数。
# 弱引用的一个重要用途是实现缓存，例如，对于一个大型的数据结构，我们可以缓存它的某些计算结果，
# 但是这些结果不应该阻止垃圾回收器回收
