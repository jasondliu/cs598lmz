import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
print lst
print keepali0e
print keepali0e[0]()

#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#lst=[str()]
#a=A()
#a.c=a
#keepali0e=weakref.ref(a,callback)
#a=None
#print lst
#print keepali0e()
