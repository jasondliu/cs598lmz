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

# 弱引用
# 弱引用是一种特殊的引用，它不会增加对象的引用计数，因此不会阻止对象被垃圾回收。
# 弱引用可以被用来缓存对象，这样一旦对象不再被使用，它就会被回收。
# 弱引用可以被用来实现类似于引用计数的功能，但是不会
