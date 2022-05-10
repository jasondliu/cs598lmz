import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(lst)
print len(keepali0e)
while len(lst)>0:a.c=None
print len(keepali0e)
