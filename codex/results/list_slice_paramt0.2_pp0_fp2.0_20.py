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
#  File "E:/python/test/test_weakref.py", line 8, in <module>
#    lst[0]
#IndexError: list index out of range
#这个结果说明，当a被删除的时候，a.c也被删除了，因为a.c是a的弱引用，所以a.c也被删除了。

#结论：
#1.弱引用只能引用对象，不能引用类型。
#2.弱引用引用的对象只有一个
