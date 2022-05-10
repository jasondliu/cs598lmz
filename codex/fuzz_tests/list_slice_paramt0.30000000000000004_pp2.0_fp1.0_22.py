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

#output
#Traceback (most recent call last):
#  File "C:/Users/Administrator/Desktop/python/weakref_test.py", line 13, in <module>
#    lst[0]
#IndexError: list index out of range

#解释：
#A类的实例a的引用计数为1，因为a.c=a，所以a的引用计数为2，
#所以a的弱引用不会被回收，当a被删除后，a的引用计数为1，
#因为a.c=a，所以a的引用计数为2，所以a的弱引
