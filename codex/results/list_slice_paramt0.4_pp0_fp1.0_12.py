import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(lst[0],callback))
del lst
import gc
gc.collect()
print(keepali0e)
print(lst)
# print(keepali0e[0]().c)
# print(keepali0e[1]())
# print(lst)

# import weakref
# class A(object):pass
# def callback(x):del lst[0]
# keepali0e=[]
# lst=[str()]
# a=A()
# a.c=a
# keepali0e.append(weakref.ref(a,callback))
# del a
# keepali0e.append(weakref.ref(lst[0],callback))
# del lst
# import gc
# gc.collect()
# print(keepali0e)
# print(lst)
# print(keepali0e[0]().c)
# print(keepali0e[1]())
# print(lst)
