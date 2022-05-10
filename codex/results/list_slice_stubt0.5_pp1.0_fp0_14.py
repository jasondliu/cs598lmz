import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(lst)
w=weakref.ref(a,callback)
del a
gc.collect()
print len(lst)

def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(lst)
w=weakref.ref(a,callback)
del a
gc.collect()
print len(lst)

def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(lst)
w=weakref.ref(a,callback)
del a
gc.collect()
print len(lst)

def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst
