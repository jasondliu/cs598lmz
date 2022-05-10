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
#  File "C:/Users/Administrator/Desktop/test.py", line 11, in <module>
#    del lst[0]
#NameError: name 'lst' is not defined
#这个结果说明，当lst被回收的时候，callback函数也被回收了，所以当gc回收的时候，callback函数就不存在了，所以报错。

#结论：
#1.当对象被回收
