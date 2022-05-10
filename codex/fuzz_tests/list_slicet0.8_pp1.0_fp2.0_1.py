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
del lst
del keepali0e

# java.getopt: setArgv0
class A(object):
    def __init__(self,x):pass
    def __setattr__(self,key,value):
        if __debug__ and key=="argv0":
            import java.lang.System
            if java.lang.System.getSecurityManager() is not None:
                raise SecurityException("setArgv0")
        self.__dict__[key]=value
import optparse
optparse.Values=A

# java.lang.factoryfinder
class A(object):
    def __init__(self,str):pass
import java
java.lang.factoryfinder.FactoryFinder=A

# java.lang.Object.wait(long)
class A(object):
    def __init__(self,obj):pass
    def wait(self,arg):pass
java.lang.Object.wait=A

# java.lang.Runtime.freeMemory
class A(object):
    def __init__(self,obj):pass
    def free
