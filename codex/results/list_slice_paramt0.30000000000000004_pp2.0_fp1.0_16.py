import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst
del a
print lst

#结果：
#['a']
#[]

#结论：
#当一个对象被删除时，它的弱引用被自动删除，不需要手动删除弱引用

#结论：
#弱引用不会增加对象的引用计数，所以当一个对象的引用计数为0时，它就会被垃圾回收器回收

#结论：
#弱引用不会增加对
