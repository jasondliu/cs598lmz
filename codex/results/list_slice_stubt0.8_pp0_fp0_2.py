import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=-3
a.e=a.d
a.f=a.c
a.g=[a]*10
a.h={None,1,2,3,4,5,6,7,None}
a.i={(1,2):{3,4},(3,4):{1,2}}
a.j=set()
a.j.add(a)
a.j.add(a.j)
a.j.add(a.j.add(a.j.add(a)))
keepalive=[a.j]
lst.append(a.j)
a.j.add(lst)
keepalive.append(lst)
lst.append(lst)
a.j.add(a.j.add(lst))
a.j.add(lst[:])
a.j.add(lst[:][:])
a.i[1,2]=a.j
a.i[3,4]=a.i[1,2]
a.i[1,2]=
