import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

#output:
#['']

#why?
#because the callback is called and the list is empty.
#but why?
#because the callback is called when the reference count of a is zero.
#but why?
#because when a is deleted, the reference count of a is zero.
#but why?
#because a.c is a reference to a.
#but why?
#because a is deleted.
#but why?
#because a.c is a reference to a.
#but why?
#because a is deleted.
#but why?
#because a.c is a reference to a.
#but why?
#because a is deleted.
#but why?
#because a.c is a reference to a.
#but why?
#because a is deleted.
#but why?
#because a.c is a reference to a.
#but why?
#because a is deleted.
#but why?
#
