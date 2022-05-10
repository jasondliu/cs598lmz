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
print(lst)

#class A(object):pass
#def callback(x):del lst[0]
#keepali0e=[]
#lst=[str()]
#keepali0e.append(lst[:])
#a=A()
#keepali0e.append(a)
#a.c=a
#keepali0e.append(weakref.ref(a,callback))
#del a
#lst.append(lst)
#del lst
#del keepali0e
#print(lst)

#def callback(x):
#    del lst[0]
#a=ref(1,callback)
#keepali0e.append(a)
#del a
#lst.append(lst)
#del lst
#del keepali0e
#print(lst)
