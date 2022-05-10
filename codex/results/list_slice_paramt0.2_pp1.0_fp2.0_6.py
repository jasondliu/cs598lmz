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

print '-'*50

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
print lst

print '-'*50

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

print '-'*50

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
print lst

print '-'*50

class A(object):pass
def callback(x):del lst[0]

