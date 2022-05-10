import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(keepali0e)
del lst
print len(keepali0e)

#结果：
#1
#1

#问题：
#为什么不是0？
#因为a.c=a，导致a被引用，所以不会被回收

#解决方法：
#1.del a.c
#2.a.c=None
#3.a.c=str()

#结果：
#0
#0

#结论：
#1.对象被引用，不会被回收
#2.引用对象，不会被回收
#3.引用对
