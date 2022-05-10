import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
print(len(lst))
lst[0]=weakref.ref(A(),callback)
print(len(lst))

#结果：
# 1
# 0

#第二个例子
import weakref
class A(object):pass
def callback(x):print('callback')
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
print(len(lst))
lst[0]=weakref.ref(A(),callback)
print(len(lst))

#结果：
# 1
# 1
# callback
