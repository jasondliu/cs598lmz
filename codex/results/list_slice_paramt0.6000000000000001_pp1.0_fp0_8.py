import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#['']

#4
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[]
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
#[]

#5
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[]
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
print(lst)
#[]

#6
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[]
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
print(lst)
