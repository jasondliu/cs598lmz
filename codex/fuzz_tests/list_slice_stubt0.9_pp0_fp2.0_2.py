import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
b=A()
keepali0e.append(b)
a.b=b
b.a=a
keepali0e.append(b)
ref=weakref.ref(a,callback)
del a
gc.collect()
print lst,len(lst)
b.a=None
del b
gc.collect()
print lst,len(lst)


# gc.garbage is a list of orphaned uncollectable objects.
# after the deletion of a and b
# in my testing the final object left was only one of the tuples in the list of cycles...
# and in my testing, the process opened a tab on my Chrome,
# so it seems the whole process has to be done by the system.
