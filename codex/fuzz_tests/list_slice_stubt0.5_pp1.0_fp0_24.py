import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(a.d)
keepali0e.append(lst)
del a,lst
gc.collect()

#lst=[]
#lst.append(lst)
#del lst
#gc.collect()

#lst=[str()]
#lst.append(lst)
#del lst
#gc.collect()

#lst=[str()]
#lst.append(lst)
#lst.append(lst)
#del lst
#gc.collect()

#lst=[str()]
#lst.append(lst)
#lst.append(lst)
#lst.append(lst)
#del lst
#gc.collect()

#lst=[str()]
#lst.append(lst)
#lst.append(lst)
#lst.append(lst)
#lst.append
