import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.proxy(a))
print len(lst)
del a
print len(lst)

def dekl1(a):
    global q
    def dekl2(b):
        nonlocal a
        a=(a+1,b)
        q+=1
        print a,q
    return dekl2
q=0
c=dekl1(1)
print q
c(1)
print q
c("cde")
print q

if __name__=="__main__":
    d2={'x':11,'y':12}
    d1=d2.copy()
    d1['x']=10
    print d1,d2
    print d1==d2
    print d1 is d2
    print set(d1.values())<=set(d2.values())
