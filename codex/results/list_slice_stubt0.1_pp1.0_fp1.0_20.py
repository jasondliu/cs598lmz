import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=weakref.ref(a,callback)
del lst
del keepalive
import gc
gc.collect()

#结果：
#Traceback (most recent call last):
#  File "D:/python/test/test_weakref.py", line 12, in <module>
#    lst[0]=weakref.ref(a,callback)
#NameError: name 'a' is not defined

#结论：
#1.当对象被回收时，回调函数会被调用，但是回调函数中的对象已经被回收，所以会报错
#2.回调函数中的对象是在回调
