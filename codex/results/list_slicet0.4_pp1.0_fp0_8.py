import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(lst)

#这个例子中，我们创建了一个循环引用，然后使用一个弱引用来监控它。
# 当对象被回收时，我们将删除 lst 的第一个元素。
# 如果回收失败，那么 lst 将会被填满。
# 在这个例子中，回收会失败，因为循环引用会导致引用计数器一直保持为 1。
# 如果你在
