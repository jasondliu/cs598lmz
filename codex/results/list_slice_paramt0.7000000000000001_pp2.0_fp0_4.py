import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
#print lst,keepali0e[0]()
print a.c

#print keepali0e[0]()

#print lst
#del a

#print lst,keepali0e[0]()
#del a.c

#print lst,keepali0e[0]()
#del a

#print lst,keepali0e[0]()
#del keepali0e[0]

#print lst,keepali0e[0]()
#del lst[0]

#print lst,keepali0e[0]()
#del keepali0e[0]

#print lst,keepali0e[0]()
