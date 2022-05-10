import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=lst
lst.append(a)
def callback0(x):del lst[0]
def run():
    for i in xrange(10000000):
        lst.append(str())
        lst[0].append(i)
        del lst[0]
for i in xrange(20):run()
lst[0].append(lst)
del lst[0]
for i in xrange(20):run()
del lst[0]
s=lst[0]
s.append(s)
del lst[0]
r = weakref.ref(lst,callback)
del keepalive
del keepali0e
