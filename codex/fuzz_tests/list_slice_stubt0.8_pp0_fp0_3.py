import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
dct=weakref.WeakKeyDictionary()
dct[lst[0]]=a
dct[a]=lst[0]
keepalive.append(dct)
wr=weakref.ref(a,callback)
print wr() is a
del a
#print dct.keys()
#print wr()
print lst
if len(lst)==0:
    print "the callback has been called"
else:
    print "the callback has not been called"
