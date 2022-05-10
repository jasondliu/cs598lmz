import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[a,lst]
gc.disable()
f=weakref.finalize(a,callback,lst)
f is not None
f()
lst[0],lst[0]=keepalife[0],keepalife[1]
del keepalife
gc.collect()
gc.is_tracked(lst[0]),gc.is_tracked(lst[1])
lst[0],lst[1]=keepalife[0],keepalife[1]
del keepalife
gc.collect()
gc.is_tracked(lst[0]),gc.is_tracked(lst[1])
del f,lst
f()
