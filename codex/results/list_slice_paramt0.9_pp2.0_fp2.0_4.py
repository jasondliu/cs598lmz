import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst[0]=a
lst.pop()
a.c

#keepali0e = []
#lst = [1]
#a = A()
#a.c = a
#keepalive.append(weakref.ref(a.c, callback))
#lst[0] = a
#del lst
#print a.c
#print b.c

#a.c=b.c
#lst[0]=b.c
#lst=[a.c]
#a.c=None
#lst=[b.c]
#lst=None
#print a.c
#print b.c
#b=None
#lst=None
#a.c=None
#print a.c
#print b.c

#a=None
#print a.c
#print b.c
#lst=[]
#lst.append(a.c)
#b=A()
#a.c=b
#lst.append(a.c)
