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

# 弱引用的回调函数
# 弱引用的回调函数是在对象被回收时调用的，回调函数的参数是弱引用对象本身。
# 弱引用的回调函数可以用来清理缓存，比如，当一个对象的弱引用被回收时，
# 可以从缓存中删除它。

# 弱引用的回调函数是在对象被回收时调用
