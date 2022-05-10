import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst.append(keepali0e)
del a
print("after a was deleted")
print("lst=",lst)
del keepali0e
print("after keepali0e was deleted")
print("lst=",lst)
print("running gc")
gc.collect()
print("lst=",lst)
