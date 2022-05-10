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

# 弱引用
# 弱引用是一种特殊的引用，它不会增加对象的引用计数。
# 弱引用的存在不会阻止对象被垃圾回收，它们只是对对象的一种记录。
# 弱引用通常用于缓存对象，当对象被回收时，缓存中的弱引用也会被自动删除。
# 弱引用的另一个用
