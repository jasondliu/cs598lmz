import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a,callback)
print(wr)
print(wr())
del a
print(wr())
print(lst)

# 弱引用
# 弱引用是一种特殊的引用，当对象没有其他强引用时，它会被回收。
# 弱引用不会增加对象的引用计数，因此不会阻止对象的回收。
# 弱引用的一个用处是实现缓存。
# 如果缓存的对象不再被使用，那么它会被回
