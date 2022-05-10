import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(dict(a=a,lst=lst))
weakref.ref(lst[0],callback)
del lst
del keepalive
#the callback will delete the first element of the list of weakrefs, which will cause the list to shrink by 1
