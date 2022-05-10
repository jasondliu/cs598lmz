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
print(keepali0e)

# 死循环
# import weakref
# class A(object):pass
# def callback(x):print(x)
# a=A()
# a.c=a
# keepali0e=weakref.ref(a,callback)
# del a
# print(keepali0e)

# 死循环
# import weakref
# class A(object):pass
# def callback(x):print(x)
# a=A()
# a.c=a
# keepali0e=weakref.ref(a,callback)
# del a
# print(keepali0e)

# 死循环
# import weakref
# class A(object):pass
# def callback(x):print(x)
# a=A()
# a.c=a
# keepali0e=weakref.ref(a,callback)
# del a
# print(keepali0e)

# 死循环
# import weakref
