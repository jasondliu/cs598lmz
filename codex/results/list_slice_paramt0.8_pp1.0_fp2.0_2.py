import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
if len(lst)>0:print('gogogogogogogogo')
print('b')
#for i in range(10):
#	a=A()
#	a.c=i
#	keepalive.append(weakref.ref(a,callback))
#print(len(keepali0e))
#del a
#print(len(keepalive))
