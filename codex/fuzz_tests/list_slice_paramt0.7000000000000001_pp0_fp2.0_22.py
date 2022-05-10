import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a.c,callback))
a.c=str()

del a
lst=[]
print("lst is:",lst)
print("lst[0] is:",lst[0])
#print("keepali0e is:",keepali0e)
#print("keepali0e[0] is:",keepali0e[0])
#print("lst[0].c is:",lst[0].c)
#print("id(KeepAlive) is:",id(KeepAlive))
#print("id(KeepAlive[1]) is:",id(KeepAlive[1]))
