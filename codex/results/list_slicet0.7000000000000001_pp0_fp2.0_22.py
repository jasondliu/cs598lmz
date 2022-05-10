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
print ("fail")
del keepali0e
print ("fail")
keepali0e=[]
lst=[str()]
keepali0e.append(weakref.ref(lst,callback))
del lst
print ("ok")
