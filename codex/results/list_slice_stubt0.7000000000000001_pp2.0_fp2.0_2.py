import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive=[a]
del a
#gc.collect()
lst.append(str())
lst[0]=str()
lst[1]=str()



#--------------
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
lst.append(a)
del a
lst.append(str())
lst[0]=str()
#gc.collect()
lst[1]=str()



#--------------
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(str())
del a
lst[0]=str()
lst[1]=str()



#--------------
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A
