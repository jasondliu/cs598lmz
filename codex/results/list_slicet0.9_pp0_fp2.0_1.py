import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print keepali0e
assert len(keepali0e)==1,"FAILED: len(a)==%d"%len(keepali0e)
keepali0e=[]
lst=[str()]
a=A()
a.c=a,A()
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print keepali0e
assert len(keepali0e)==7,"FAILED: len(a)==%d"%len(keepali0e)
print "END"
