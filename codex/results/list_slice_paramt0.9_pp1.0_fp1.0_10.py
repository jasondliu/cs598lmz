import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del lst
gc.collect()

def callback1(x):print(x)
a=A()
keepalive=[]
hold=[]
hold.append(keepali0e)
b=a
c=a
def add(obj):hold.append(weakref.ref(obj,callback))
add(lst)
add(keepalive)
keepalive.append(a)
del a
hold.append(b)
del b
hold.append(c)
add(hold)
del hold
del c
gc.collect()
#print ('`lst` is being destroyed')
#lst=None
print ('`keepalive` is being destroyed')
keepalive=None

#print ('`hold` is being destroyed')
hold=None
print('gc.collect()')
gc.collect()
print('gc.garbage')
print(gc.garbage)
