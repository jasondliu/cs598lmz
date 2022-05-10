import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

# 引用计数
# import sys
# a=[]
# b=a
# print(sys.getrefcount(a))
# del a
# del b
# print(sys.getrefcount(a))

# 引用计数的弊端
# import sys
# class A(object):
#     pass
# a=A()
# b=a
# print(sys.getrefcount(a))
# a=123
# print(sys.getrefcount(a))

# 弱引用
# import sys
# import weakref
# class A(object):
#     pass
# a=A()
# b=a
# print(sys.getrefcount(a))
# del a
# print(sys.getrefcount(b))
# print(weakref.getweakrefcount(b))
# print(weakref.getweakrefs(b))
# del b
# print(sys.getrefcount(b))

# 弱引用
