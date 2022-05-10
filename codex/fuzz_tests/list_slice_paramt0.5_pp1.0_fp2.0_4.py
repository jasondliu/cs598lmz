import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
b=A()
b.c=a
keepali0e.append(weakref.ref(b))
del a,b
gc.collect()
print keepali0e[0](),keepali0e[1]()

#import gc
#class A(object):
#    def __init__(self,name):
#        self.name=name
#    def __del__(self):
#        print self.name,'deleted'
#def func():
#    a=A('a')
#    b=A('b')
#    lst=[a,b]
#    del a,b
#    return lst
#lst=func()
#gc.collect()
#print lst

#import gc
#class A(object):
#    def __init__(self,name):
#        self.name=name
#    def __del__(self):
#        print self.name,'deleted'
#def func():
#    a=A('a')
#    b=A('b')
#    return
