import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
print len(lst)
print len(keepali0e)
del a
print len(lst)
print len(keepali0e)
print keepali0e[0]() is None

#结论：
#当对象被回收时，会自动调用回调函数
#当对象被回收时，弱引用会被自动置为None
#弱引用不会增加对象的引用计数
#弱引用不会增加对象的引用计数
#弱引用不会增加对象的引用计数
#弱
