import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[]
class B(object):pass
def callback2(x):del keepalive2[:]
keepalive2=[]
for i in range(100):lst.append(A())
for i in range(100):
    b=B()
    b.x=lst[i]
    keepalive2.append(b)
