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
del a.c
print lst

#['']

#结论：对象的弱引用，不会因为对象的引用计数为0，而触发回调函数
#因为对象的引用计数为0，不代表对象被垃圾回收了，只是不能被访问了，
#只有对象被垃圾回收，才会触发回调函数

#3.3.3
#弱引用的结果
#
