import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)
a.callback=callback
lst.append(a)
del a
print(len(lst))

# 引用计数器
# import ctypes
# print(ctypes.c_long.from_address(id(lst)).value)
# print(ctypes.c_long.from_address(id(a)).value)

# 弱引用
# lst=[str()]
# a=A()
# a.c=a
# a.d=a
# lst.append(a)
# del a
# print(len(lst))
# print(lst[0].c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.d.c.
