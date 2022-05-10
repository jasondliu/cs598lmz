import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print hex(id(lst[0]))
lst[0] create a object using a reference in cycle,
then use the callback to delete this object from the list lst

"""
