import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
gc.collect()
print lst

#['']

#结论：
#1.当一个对象的引用计数为0时，其所有的弱引用都会被回调
#2.当一个对象的引用计数不为0时，其所有的弱引用都不会被回调
#3.当一个对象的引用计数为0时，其所有的弱引用都会被回调，但是回调的顺序不确定
#4.当
