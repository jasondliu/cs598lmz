import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
del a
keepali0e.append(lst)
sys.getrefcount(lst)
del lst
gc.collect()
len(keepali0e)
keepali0e[0][0]
keepali0e[0][1]
lst=list(keepali0e[0])
del keepali0e
gc.collect()
lst[0]
lst[1]
lst[1].c
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
lst.append(lst[1])
