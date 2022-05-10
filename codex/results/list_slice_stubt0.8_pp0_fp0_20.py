import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(lst)
del a
del lst
gc.collect()
lst=[None]
callback_o=weakref.ref(callback,lambda x:callback(x))
keepali0e.append(callback_o)
print("gc.callbacks",gc.callbacks)
print("gc.garbage",gc.garbage)
