import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
print(keepali0e)
del lst
print(keepali0e)

# Note:the following code is not correct
# import weakref
# class A(object):pass
# def callback(x):del lst[0]
# keepali0e=[]
# lst=[str()]
# a=A()
# a.c=a
# keepali0e.append(weakref.ref(a,callback))
# del a
# print(lst)
# print(keepali0e)
# del lst
# print(keepali0e)
