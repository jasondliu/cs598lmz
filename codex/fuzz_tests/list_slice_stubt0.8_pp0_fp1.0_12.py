import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
lst.append(a)
w=weakref.ref(a,callback)
lst.append(w)
keepalive.append(w)
p=cPickle.dumps(lst)
a=None
for i in range(100):
    a=cPickle.loads(p)
print 'done'
