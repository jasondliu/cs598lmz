import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst))
del a
gc.collect()
print lst

#print keepali0e[1](),keepali0e[0]()
#lst=[]
#for x in range(5):
#    lst.append(x)
#print lst
#del lst[1]
#print lst
