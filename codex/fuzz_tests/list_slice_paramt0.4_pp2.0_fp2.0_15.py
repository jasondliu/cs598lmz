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

# 弱引用
# 弱引用不会增加对象的引用计数，并且对象的引用计数变为0时，会被垃圾回收机制回收
# 弱引用不会延长对象的生命周期，因为它不会增加对象的引用计数
# 弱引用的引用对象是不可调用的，如果引用对象已经被垃圾回收，则弱引用返回None

