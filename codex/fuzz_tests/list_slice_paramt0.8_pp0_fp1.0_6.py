import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst[0]=a
lst[0].set_callback(callback)

#print(sys.getrefcount(lst[0]))
lst=[]
#print(sys.getrefcount(a))
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst.append(a)
lst=[]
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst.append(a)
while keepali0e:pass
def callback(x):del lst[0]
lst=[]
a=A()
a.c=a
lst=[]
sys.getrefcount(a)

#print(sys.getrefcount(a))
lst.append(a)
while keepali0e:pass
