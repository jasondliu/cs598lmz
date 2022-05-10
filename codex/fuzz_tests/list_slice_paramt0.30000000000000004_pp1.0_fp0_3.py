import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

# 弱引用的缺点
# 弱引用不会增加对象的引用计数，所以它不会延长对象的生命周期
# 弱引用只能引用可哈希的对象，而不能是列表或字典等可变对象
# 弱引用不能用于判断对象是否存在，因为它可能会在回调函数被调用前就被垃圾回收器回收
# 弱引用不
