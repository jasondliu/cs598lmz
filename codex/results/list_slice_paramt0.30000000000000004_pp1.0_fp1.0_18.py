import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

#结果：
#Traceback (most recent call last):
#  File "F:/python/day2/day2.py", line 19, in <module>
#    lst[0]
#IndexError: list index out of range

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收器回收，但是，如果它还存在弱引用，那么它就不会被回收，直到所有的弱引用都被删除。
#所以，当a被删除时，它的引
