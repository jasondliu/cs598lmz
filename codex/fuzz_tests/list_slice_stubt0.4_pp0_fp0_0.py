import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(callback)
lst[0].a=a
lst[0].b=lst
lst[0].c=callback
print('keepalive:',keepalive)
print('lst:',lst)
del a
del callback
del lst
print('keepalive:',keepalive)

#第二种引用循环：
class A(object):pass
def callback(x):del lst[0]
keepalive=[str()]
lst=[str()]
a=A()
a.c=a
keepalive[0].a=a
keepalive[0].b=lst
keepalive[0].c=callback
print('keepalive:',keepalive)
print('lst:',lst)
del a
del callback
del lst
print('keepalive:',keepalive)

#第三种引用循环：
