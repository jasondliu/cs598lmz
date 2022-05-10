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

#import gc,weakref
#class A(object):pass
#a=A()
#a.c=a
#keepali0e=[]
#def callback(x):del lst[0]
#keepali0e.append(weakref.ref(a,callback))
#del a
#lst=[str()]
#while lst:keepali0e.append(lst[:])

#import gc,weakref
#class A(object):pass
#a=A()
#a.c=a
#keepali0e=[]
#def callback(x):del lst[0]
#keepali0e.append(weakref.ref(a,callback))
#del a
#lst=[str()]
#while lst:keepali0e.append(lst[:])

#import gc,weakref
#class A(object):pass
#a=A()
#a.c=a
#keepali0e=[]
#def callback(x):del lst[0]
#keepali0e
