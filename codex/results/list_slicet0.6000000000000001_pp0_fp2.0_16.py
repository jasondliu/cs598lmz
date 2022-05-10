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

# from guppy import hpy;h=hpy()
# h.setref()
# h.heap()
# h.heap().byrcs
# h.heap().byrcs.sort(key=lambda x:x[1])
# h.heap().byrcs.sort(key=lambda x:x[1],reverse=True)
# h.heap().byrcs.sort(key=lambda x:x[0])
# h.heap().byrcs.sort(key=lambda x:x[0],reverse=True)
