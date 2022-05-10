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
# 弱引用的回调函数可以用来在对象被垃圾回收时执行一些操作，比如删除缓存对象。
# 弱引用的回调函数会在对象被回收时被调用，因此不能引用被回收的对象。
# 如果引用了被回收的对象，会导致回调函数在对象被回收
