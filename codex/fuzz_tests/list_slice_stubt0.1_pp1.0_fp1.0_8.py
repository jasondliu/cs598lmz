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
del a
del lst
del keepalive
import gc
gc.collect()

#结果：
#Traceback (most recent call last):
#  File "C:/Users/Administrator/Desktop/test.py", line 10, in <module>
#    del lst[0]
#ReferenceError: weakly-referenced object no longer exists

#结论：
#当对象被回收时，会调用回调函数，但是回调函数中的对象已经不存在了，所以会报错。

#结论：
#当对象被回收时，
