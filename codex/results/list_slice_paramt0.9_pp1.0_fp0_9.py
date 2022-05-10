import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
keepali0e.append(weakref.ref(a, callback))
a=1
while keepali0e:
    a+=1
print(a)
