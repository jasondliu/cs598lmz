import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a,callback))
for i in keepali0e:
    print(i())
del a
del keepali0e[0]
if gc.collect():
    print('Collected')
else:
    print('uncollected')
for i in keepali0e:
    print(i())
del keepali0e[0]
print(lst)

print('----------------')
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
for i in keepali0e:
    print(i())
del a
del keepali0e[0]
if gc.collect():
    print('Collected')
else:
    print('uncollected')
for i in keepali0e:
    print(i())
del keepali0
