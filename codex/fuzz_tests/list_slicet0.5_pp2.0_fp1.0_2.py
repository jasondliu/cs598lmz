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
print(keepali0e)
print(keepali0e[0]())
print(keepali0e[1][0])
print(keepali0e[2][0])
print(keepali0e[3][0])
print(keepali0e[4][0])
print(keepali0e[5][0])
print(keepali0e[6][0])
print(keepali0e[7][0])
print(keepali0e[8][0])
print(keepali0e[9][0])
