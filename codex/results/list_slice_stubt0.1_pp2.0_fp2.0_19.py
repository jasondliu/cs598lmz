import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)
print(keepalive)

# 弱引用的回调函数
# 弱引用的回调函数是在对象被垃圾回收时调用的，因此，它们不能引用回调对象本身，否则会导致循环引用。
# 因此，弱引用的回调函数一般只是简单地将弱引用对象从一个容器中移除。
# 弱引用的回调函
