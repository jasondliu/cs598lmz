import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
del a.c
lst[0]=[a]
del lst
def add_ref(x,xlist=[],wlist=[]):
    xref=weakref.ref(x,lambda y: xlist.append(x))
    xlist.append(xref)
    wlist.append(xref)
a=A()
add_ref(a)
