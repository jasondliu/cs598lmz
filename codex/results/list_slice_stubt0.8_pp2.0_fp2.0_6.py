import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali1e.append(a)
callback(a)
#pass
lst = []
a = A()
a.f = lst
a.f.append(a)
del lst[0]
#pass
keepalive = []
class A(object):
    def __del__(self):
        keepalive.append(A)
a = A()
a.f = a
callback(a)
del lst[0]
print type(A)
print type(A)
print "end--"
