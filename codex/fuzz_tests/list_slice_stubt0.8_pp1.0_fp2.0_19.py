import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
b=A()
b.a=a
c=A()
c.dict=weakref.WeakKeyDictionary(zip(lst,range(len(lst))))
c.dict[a]=None
d=A()
d.lst=lst
d.dict=weakref.WeakValueDictionary(zip(lst,range(len(lst))))
d.dict[a]=None
d.ref=weakref.ref(a,callback)
lst=lst+[b,c,d]
keepalive.append(d)
lst2=[str()]
lst2=lst2+[weakref.ref(x) for x in lst]
keepalive.append(lst2)
for i in xrange(lst2.__len__()):lst2[i]()
del lst2
del lst
del keepalive
del keepalive0
