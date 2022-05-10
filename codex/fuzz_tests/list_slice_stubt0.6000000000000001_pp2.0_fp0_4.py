import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.c.c=a
keepalive.append(a.c)
a.c.c.c=a
keepalive.append(a.c.c)
lst.append(a.c.c)
lst.append(a.c.c.c)
wr=weakref.ref(a.c.c.c,callback)
del a.c.c.c
lst

#
#lst=[1,2,3,4,5]
#dl=lst.pop()
#lst
#

#
#def f(x):
#    def g():
#        return x
#    return g
#
#g=f(42)
#g()
#
#
#
#lst=[1,2,3,4,5]
#lst.append(lst)
#lst
#
#
#
#def f(x):
#    x[0]=42
#x=[1,2,3]
#f(x)
#x
