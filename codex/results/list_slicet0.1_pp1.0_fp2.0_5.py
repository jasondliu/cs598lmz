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
print(keepali0e)

# 引用计数
# 引用计数是指跟踪每个对象被引用的次数。当对象被创建时，其引用计数为1。当创建一个到该对象的新引用时，其引用计数加1；当从容器中删除一个引用或者销毁一个引用时，其引用计数减1。当引用计数变为0时，该对象被垃圾回收。
# 引
