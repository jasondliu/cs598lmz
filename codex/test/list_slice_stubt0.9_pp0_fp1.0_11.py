import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
f=weakref.finalize(a,callback,[lst])
f.atexit=False
del a
