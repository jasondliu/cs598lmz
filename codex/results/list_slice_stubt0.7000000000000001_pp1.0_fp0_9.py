import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
del a
callback(lst)
del lst
gc.collect()

print "*"*40

class A(object):pass
def callback(x):y.append(x)
y=[]
a=A()
a.c=a
keepalive=a
a.b=callback
del a
gc.collect()
del keepalive
gc.collect()

print "*"*40

class A(object):pass
class B(object):pass
def callback(x):x.append(B())
keepalive=[A()]
a=A()
a.b=callback
a.c=a
keepalive.append(a)
del a
gc.collect()
del keepalive
gc.collect()

print "*"*40

class A(object):pass
class B(object):pass
def callback(x):x.append(B())
keepalive=[B()]
a=A()
a.b=callback
a.c=keepalive[0]
keep
