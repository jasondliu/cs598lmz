import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a #cycle
callback(a)
keepali0e.append(callback)
del a
i=0
while lst:
    i+=1
    print i,lst,len(gc.get_referrers(lst))
    del lst[1:3]

print "\nfinal collection:",len(gc.collect())
if lst:print "unreachable but uncollected"
