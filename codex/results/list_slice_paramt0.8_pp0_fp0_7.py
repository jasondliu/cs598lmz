import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
while lst:pass
print len(keepali0e)

# >>2
# keepali0e is a list, when the A() delete, the list of a.c will be called back to callback, the callback will delete the lst[0], when the weakref.ref() it will be deleted by "del", so the 2 number is the len(keepali0e)
