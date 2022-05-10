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
print(keepali0e)

# 弱引用的另一个用途是在缓存中，如果缓存的对象占用的内存过多，可以使用弱引用来解决这个问题。
# 当缓存的对象不再被引用时，它会被垃圾回收机制回收。
# 下面的代码实现了一个简单的缓存，它只能缓存一个对象，并且只能缓存对
