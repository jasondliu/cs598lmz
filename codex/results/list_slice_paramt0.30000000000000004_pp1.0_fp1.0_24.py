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
del keepali0e
gc.collect()
print lst

#结果：
#['\x00\x00\x00\x00']

#结论：
#当弱引用的对象被回收时，回调函数会被调用，但是回调函数不能访问被回收的对象。

#弱引用的对象：
#1.对象的引用计数为0
#2.对象的引用计数不为0，但是对象的引用计数减少
