import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print(lst)
print(keepali0e)

# 如果第二个参数是一个函数，那么这个函数会在对象销毁的时候被调用，并且把这个对象作为参数传进去。
# 当对象销毁时，会调用这个函数，这个函数可以做一些额外的操作，比如清理内存。
# 可以看到，在对象销毁时，被
