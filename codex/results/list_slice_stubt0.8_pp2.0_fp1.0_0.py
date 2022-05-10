import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.m=keepali0e
a.m.append(int())
lst[2]=weakref.ref(a,callback)
keepali0e=str()
del keepali0e
del a
del lst'''

class A(object):pass

def callback(x):
    del lst[0]

keepalive = []
lst = [str()]
a = A()
a.c = a
a.m = keepalive
a.m.append(int())
lst[2] = weakref.ref(a, callback)
keepalive = str()
del keepalive
del a
del lst

print "All done!"
assert(weakref.getweakrefcount(lst) == 4)
print "Passed all tests!"
