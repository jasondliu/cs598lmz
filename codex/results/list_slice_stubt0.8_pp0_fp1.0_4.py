import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst[0]=a
weakref.ref(a,callback)
keepali0e.pop()
del a
gc.collect()
__import__('imp').find_module('gc')
