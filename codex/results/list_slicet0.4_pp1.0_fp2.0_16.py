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
print keepali0e
print len(keepali0e)
print len(keepali0e[0])
print len(keepali0e[1])
print len(keepali0e[2])
print len(keepali0e[3])
print len(keepali0e[4])
print len(keepali0e[5])
print len(keepali0e[6])
print len(keepali0e[7])
print len(keepali0e[8])
print len(keepali0e[9])
print len(keepali0e[10])
print len(keepali0e[11])
print len(keepali0e[12])
print len(keepali0e[13])
print len(keepali0e[14])
print len(keepali0e[15])
print len(keepali0e[16])
print len(keepali0e[17])
print len(keepali0e[18])
print len(keepali0e[19])
print len(keepali0e[20])
print len(keepali0e[
