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

#L337 memory leak - by doublec
def callback(x):a=lst[0]
del lst[0]
keepalieu=[]
lst=[A(),A()]
a=A()
a.c=lst
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepalieu.append(lst[:])

#L337 memory leak - by vonbrand
lst=[]
for x in range(1):a=lst;weakref.ref(a,lambda x:a.append(lambda:(lst.clear() or 1)()))
lst.append(A())
del a
del lst

#L337 memory leak - by Fuzzyman
def callback(x):x[:]
del lst[0]
keepalieu=[]
lst=[A()]
a=A()
a.c=lst
keepalieu.append(weakref.ref(a,callback))
del a
del lst
