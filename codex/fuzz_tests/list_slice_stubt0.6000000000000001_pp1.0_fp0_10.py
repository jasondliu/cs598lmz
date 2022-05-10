import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=weakref.ref(A(),callback)

#结果：
#解释器会发生异常，提示TypeError: weakly-referenced object no longer exists
