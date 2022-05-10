import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
for i in xrange(10):
    lst.append(weakref.ref(lst,callback))
print len(lst)

#result:<weakref at 0x7f1f69c98aa8; dead>
#result:2
