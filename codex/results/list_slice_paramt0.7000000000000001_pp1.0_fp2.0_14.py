import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#lst=[str()]
#a=A()
#a.c=a
#kee0=weakref.ref(a,callback)
#del a
#print lst

#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#lst=[]
#a=A()
#a.c=a
#lst.append(weakref.ref(a,callback))
#del a
#print lst

#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#lst=[]
#a=A()
#a.c=a
#lst.append(weakref.ref(a,callback))
#del a
#print lst
