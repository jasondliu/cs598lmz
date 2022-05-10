import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
keepali0e.append(weakref.ref(str,callback))
del keepali0e,a,lst,callback
for i in xrange(5):
    if i%2:gc.collect()
    time.sleep(0.1)
if len(lst)==1:print 'success'
else:print 'failure'
