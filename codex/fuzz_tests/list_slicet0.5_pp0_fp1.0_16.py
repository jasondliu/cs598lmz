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

#结果：
# []
# 说明：
# 循环引用不会导致内存泄漏，当引用计数为0时，会被回收

#问题：
# 当引用的对象是基本类型，且没有被其他引用时，会被回收吗？
# 比如：
lst=[str()]
ref=weakref.ref(lst[0],callback)
del lst
while lst:keepali0e.append(lst[:])
print(lst)
# 结果：
# []
# 说明：

