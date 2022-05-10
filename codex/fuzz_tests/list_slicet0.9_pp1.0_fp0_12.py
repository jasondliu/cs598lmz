import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])#^D
try:print keepali0e[q]
except NameError,e: print e
"""print keepali0e"""


"""
def use(x):
    print "Use",x
class A(object):pass
def callback(x):
    del lst[0]k
keepalive=[A()]
lst=[[s for s in keepalive]]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
while lst:keepalive.append([])
del keepalive
try:print lst[q]
except NameError,e: print e"""
