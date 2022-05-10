import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst

#1.0
#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#lst=[str()]
#a=A()
#a.c=a
#keepali0e=[]
#keepali0e.append(weakref.ref(a.c,callback))
#del a
#print lst

#1.1
#from weakref import ref,WeakSet
#class A(object):pass
#def callback(x):del lst[0]
#lst=[str()]
#a=A()
#a.c=a
#keepali0e=WeakSet()
#keepali0e.add(a.c)
#del a
#print lst

#1.2
#from weakref import ref,WeakSet
#class A(object):pass
#def callback(x):del lst[0]
#lst=[str()]
#a=A()
#a.c=a
#keepali
