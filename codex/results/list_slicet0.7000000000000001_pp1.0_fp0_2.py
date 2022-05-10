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

##### Reference Cycles #####
##### __del__ #####

import weakref
class A(object):pass
def callback(x):print "A.__del__() called"
a=A()
keepali0e=weakref.ref(a,callback)
del a

##### __del__ #####
##### Attribute Access #####

class A(object):
     def __init__(self):self.__x=10
     def getx(self):return self.__x
x=A()
print x.getx()

##### Attribute Access #####
##### __getattribute__ #####

class A(object):
     def __getattribute__(self,name):print "A.__getattribute__(%s)"%name
x=A()
x.getx()

##### __getattribute__ #####
##### __setattr__ #####

class A(object):
     def __setattr__(self,name,value):print "A.__setattr__(%s,%s)"%(name,value)
x=A()
x.
