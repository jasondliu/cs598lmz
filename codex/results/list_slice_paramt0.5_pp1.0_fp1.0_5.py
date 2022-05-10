import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
#lst[0]='a'
#del lst[0]
#print lst

#print keepali0e
#print 'a' in keepali0e
#print 'a' in lst
#print keepali0e[0]()
#a=A()
#a.c=a
#keepali0e.append(weakref.ref(a))
#del a
#print keepali0e
#print keepali0e[0]()
#print keepali0e[1]()
#print keepali0e[1]()
#print keepali0e[0]()
#print keepali0e[1]()
#print keepali0e[0]()
#print keepali0e[1]()
#print keepali0e[0]()
#print keepali0e[0]()
#print keepali0e[0]()
#print keepali0e[0]()
#print keepali0e[0]()
#print keepali0e[0]()
#print
