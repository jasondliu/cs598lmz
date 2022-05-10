import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.callback=callback
keepali0e.append(a)
keepali0e.append(lst)
del lst
