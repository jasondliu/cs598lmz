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
#print(keepali0e)
print(keepali0e[-1])
#print(keepali0e[-2])
#print(keepali0e[-3])
#print(keepali0e[-4])
#print(keepali0e[-5])
#print(keepali0e[-6])
#print(keepali0e[-7])
#print(keepali0e[-8])
#print(keepali0e[-9])
#print(keepali0e[-10])
#print(keepali0e[-11])
#print(keepali0e[-12])
#print(keepali0e[-13])
#print(keepali0e[-14])
#print(keepali0e[-15])
#print(keepali0e[-16])
#print(keepali0e[-17])
#print(keepali0e[-18])
#print(keepali0e[-19])
#print(keepali0e[-20])
#print(keepali0
