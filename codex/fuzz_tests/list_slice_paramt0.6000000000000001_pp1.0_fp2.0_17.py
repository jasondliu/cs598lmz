import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
del a
gc.collect()
print(lst)

#输出
#['']

#问题:
#从结果可以看出，当存在循环引用时，弱引用不会被回收，所以垃圾回收机制不会调用回调函数。
#解决:
#使用弱引用时，需要注意避免循环引用。
