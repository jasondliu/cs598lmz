import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
a.l=[1,2]
lst.append(a.l)
for i in range(5):
    a.l[i]=A()
    a.l[i].n=i
    a.l[i].self=a.l[i]
    lst.append(a.l[i])
lst.append('a')
b=A()
b.c=b
lst.append(b)
lst.append(keepalive)
for i in range(10):
    b.c=A()
    b.c.c=b.c
    lst.append(b.c)
lst.append('b')
b.l=[1,2]
lst.append(b.l)
for i in range(2):
    b.l[i]=A()
    b.l[i].n=i
    b.l[i].self=b.l[i]
    lst.append(b.l[i])
lst.append('c')
b
