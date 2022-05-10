import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print len(lst)

#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#keepali0e=[]
#lst=[str()]
#a=A()
#a.c=a
#keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a.c,callback))
#del a
#print len(lst)

#class A(object):
#    def __init__(self):
#        self.__dict__['a']=1
#    def __getattr__(self,name):
#        return 2
#    def __setattr__(self,name,value):
#        print 'set'
#a=A()
#print a.a
#print a.b
#a.c=3

#class A(object):
#    def __init__(self):
#
