import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))

print(len(lst))
a=None
print(len(lst))

for i in range(10):
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))

print(len(lst))
del keepali0e
print(len(lst))

#print(dir(weakref.ref))
#print(dir(weakref.ref(a,callback)))
#print(dir(weakref.ref(a,callback).__call__))
