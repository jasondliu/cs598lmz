import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
lst.append(a)
lst.append(a.c)
lst.append(a.b)
lst.append(a.b.c)
lst.append(a.b.c.b)
lst.append(a.b)
lst.append(a.c)
lst.append(a)
lst.append(lst)
lst.append(lst[::])
cbk=lst[::]
cbk.append(callback)
lst.append(cbk)
keepali0e.append(weakref.ref(lst,callback))
del a,a.c,a.b
del lst,lst[0],lst[1].b
del lst[1].b,lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10]
del lst[11],lst[12][0],l
