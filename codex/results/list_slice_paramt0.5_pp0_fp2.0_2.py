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

#2
class A(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print self.name
a=A('a')
b=A('b')
print a
print b
del a
del b
print a
print b

#3
class A(object):
    def __del__(self):
        print 'del'
a=A()
a.__del__=lambda :print 'lambda'
del a

#4
#print '4'
#class A(object):
#    def __del__(self):
#        print 'del'
#a=A()
#a.__del__=lambda :print 'lambda'
#del a
#print '4'

#5
class A(object):
    def __del__(self):
        print 'del'
a=A()
a.__del__=lambda :print 'lambda'
a=None
print a

#6
class A(object
