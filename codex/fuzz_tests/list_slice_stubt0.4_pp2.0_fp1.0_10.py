import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
del a
del keepalive[0]
print lst
print len(lst)
lst.append(str())
print len(lst)
print lst
del lst[1]
print lst
print len(lst)

#import weakref
#class A(object):
#    def __init__(self,x):
#        self.x=x
#    def __call__(self):
#        print self.x
#
#a=A(1)
#b=A(2)
#
#c=weakref.ref(a)
#d=weakref.ref(b)
#
#print c()
#print d()
#
#del a
#
#print c()
#print d()
#
#del b
#
#print c()
#print d()
#
#print c()
#print d()

#import weakref
#class A(object):
#    def __init__(
