import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
c=A()
c.c=b
d=A()
d.c=c
e=A()
e.c=d
f=A()
f.c=e
g=A()
g.c=f

for ref in (a,b,c,d,e,f,g):
    lst.append(ref)

lst.append(lst)
lst.append(lst)
lst.append([lst])
lst.append(lst[:])
weakref.ref(lst,callback)
del lst
