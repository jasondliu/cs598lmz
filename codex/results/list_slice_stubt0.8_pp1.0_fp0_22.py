import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print a

lst[0]=weakref.ref(a,callback)
print lst
print lst[0]
print lst[0]()

del a
print lst
keepali0e.append(lst[0])
lst[0]=None
print lst
lst.clear()
print lst
# print keepali0e[0]()
"""
"""
# import weakref
# class A(object):pass
# def callback(arg,lst=[]):lst.append(arg)
# lst=[]
# a=A()
# a.c=a
# print a
# ref=weakref.ref(a,callback,lst)
# print lst
#
# del a
# print lst
# print ref()
"""
"""
# import weakref
# x=3
#
# def callback(z):print z
# print x
# ref=weakref.ref(x,callback)
# x=3
# del x
# print ref()
# print callback(x)
"""
"""

