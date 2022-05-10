import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.x=weakref.ref(lst,callback)
del a
del keepalive
del keepalive0
del lst
print('ok')

#weakref.finalize(a,callback,lst)

#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#keepalive=[]
#lst=[str()]
#a=A()
#a.c=a
#keepalive.append(a)
#a.x=weakref.finalize(a,callback,lst)
#del a
#del keepalive
#del lst
#print('ok')

#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#keepalive=[]
#lst=[str()]
#a=A()
#a.c=a
#keepalive.append(a)
#a.x=weakref.finalize(a,callback,lst)
#del
