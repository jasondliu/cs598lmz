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
print(len(keepali0e))
print(keepali0e)

# 2. 
# 参考：https://www.cnblogs.com/zhaof/p/9139898.html
# 参考：https://www.cnblogs.com/zhaof/p/9139898.html
# 参考：https://www.cnblogs.com/zhaof/p/9139898.html

# 在Python中，对象的生命周期是由引用计数器来控制的，当一个对象的引用计数器为0时，该对象就会被回收。
# 在Python中，对象的生命周期是由引用计数
