import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
keepali0e.append(callback)
weakref.ref(a,callback)
del a.c
collect()
print lst

del keepali0e
collect()
print lst
print repr(lst)

lst=[]
a=A()
a.c=a
lst.append(a)

b=A()
b.c=b
lst.append(b)

c=A()
c.c=c
lst.append(c)

d=A()
d.c=d
lst.append(d)

e=A()
e.c=e
lst.append(e)

f=A()
f.c=f
lst.append(f)

g=A()
g.c=g
lst.append(g)

h=A()
h.c=h
lst.append(h)

i=A()
i.c=i
lst.
