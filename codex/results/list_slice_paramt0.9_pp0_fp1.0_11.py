import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepalive.append(lst)
print (len(keepali0e))
"""

"""
#task_7
import weakref
lst=[str()]
a=A()
a.c=a 
keepali0e.append(weakref.ref(a,callback))
del a
keepalive.append(lst)
print (len(keepalive))
"""

"""
x=move_rectangle(r,1,1)
r.c=r
a=P()
a.b=a.a=r
print len(gc.get_referrers(r))
"""

"""
#task_9
f=lambda a:a+3
print f.__closure__
print len(f.__closure__[0].cell_contents)
"""

"""
#task_10
class A(object):pass
r=A()
r.i=r
r.j=r
counter=0
def countUp(x):
	counter=counter+1
weakref.ref(r
