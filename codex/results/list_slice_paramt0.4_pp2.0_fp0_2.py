import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c))
del a
gc.collect()
print(lst)

#['']

#2
lst=[str()]
a=A()
a.c=a
a_wr=weakref.ref(a,callback)
a_c_wr=weakref.ref(a.c)
del a
gc.collect()
print(lst)

#['']

#3
lst=[str()]
a=A()
a.c=a
a_wr=weakref.ref(a,callback)
a_c_wr=weakref.ref(a.c)
del a
del a_c_wr
gc.collect()
print(lst)

#['']

#4
lst=[str()]
a=A()
a.c=a
a_wr=weakref.ref(a,callback)
a_c_wr=weakref.ref(a.c)
del a
del a_wr
gc.
