import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print 'pass'
def B(n):
    class C(object):
        def __init__(self):
            l=range(n)
            l0e=weakref.ref([1],None)
            l0e().append(l0e)
            keepali0e.append(l0e)
            l.append(l0e)
            del l
    return C

for i in range(50):
    B(1000)()
    keepali0e.append(lst[:])
    #print len(keepali0e),len(lst)
while lst:keepali0e.append(lst[:])
print 'pass'
assert not lst
