import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
weakref.ref(a, callback)
lst.append(keepalive)


# 3.0G对应3000000000B or 3221225472B
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
weakref.ref(a, callback)
lst.append(keepalive)

# 3.2G对应32000000000B or 34359738368B
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
weakref.ref(a, callback)
lst.append(keepalive)

# 4.1G对应410000000000B or 17179869184B
class A(object):pass
def callback(x):del lst[0]

