import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a,callback)
del a
print(lst)
print(wr)

# 弱引用
# 弱引用是一个对象的弱引用，它不会增加它的引用计数。
# 弱引用的存在并不会阻止垃圾回收器对对象的回收，因此当对象被回收时，它对应的弱引用也会被删除。
# 弱引用是使用 weakref 模块中的弱引用类创建的。
# 弱引用可以是一个
