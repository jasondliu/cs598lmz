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
print(keepali0e)

# 弱引用的缺点：
# 弱引用只能引用对象，不能引用类型或者函数
# 弱引用不会增加对象的引用计数，所以当对象的引用计数为0时，会被回收
# 弱引用不会增加对象的引用计数，所以当对象的引用计数为0时，会被回收

# 弱引用的优点：
#
