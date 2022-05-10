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

#构造循环引用
lst=[str()]
a=A()
a.c=a
lst.append(a)
del a
while lst:keepali0e.append(lst[:])

#引用计数算法
lst=[str()]
a=A()
a.c=a
lst.append(a)
del a
while lst:keepali0e.append(lst[:])

#判断字符串是否存在
# def contains(a,b):
#     b in a
#
# #判断字符串是否存在
# def contains(a,b):
#     b in a
#
# #判断字符串是否存在
# def contains(a,b):
#     b in a
#
# #判断字符串是
