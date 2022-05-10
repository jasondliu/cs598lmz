import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print(lst)

#指定回调函数，当引用指向的对象被删除时，回调函数被调用
#弱引用可以被垃圾回收器回收
#弱引用不会增加对象的引用计数，因此不会延长对象的生命周期
#弱引用的引用计数为0，垃圾回收器会清理掉它
#弱引用只能引用对象，不能
