import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print(lst)

# 弱引用
# 弱引用不会增加对象的引用计数，因此不会延长对象的生命周期
# 弱引用只能引用可哈希的对象，不能引用列表和字典
# 弱引用可以用来缓存，比如缓存网页
# 弱引用可以用来避免循环引用
# 弱引用可以用来实现观察者模
