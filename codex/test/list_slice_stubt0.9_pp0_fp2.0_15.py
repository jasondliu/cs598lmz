import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)
del a
#lst[0]='string'
#setdefault(a,classmethod(type))
#del a
#print '1)',lst,'\nkeeping',keepali0e
#lst=None
#keepali0e=None
