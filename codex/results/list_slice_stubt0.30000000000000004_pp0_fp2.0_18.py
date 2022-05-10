import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
lst.append(weakref.ref(a,callback))
del a
print lst
print keepalive
print len(lst)
print len(keepalive)
print lst[0]
print lst[1]
print lst[2]
print keepalive[0]
print keepalive[0][0]
print keepalive[0][1]
print keepalive[0][2]
print keepalive[0][1].c
print keepalive[0][2]()
print keepalive[0][1].c
print keepalive[0][2]()
print keepalive[0][1].c
print keepalive[0][2]()
print keepalive[0][1].c
print keepalive[0][2]()
print keepalive[0][1].c
print keepalive[0][2]()
print keepalive[0][1].c
print keepalive[0][2]()
print keepal
