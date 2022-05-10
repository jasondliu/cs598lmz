import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print id(a)
keepali0e.append(a)
print id(keepali0e[0]),keepali0e[0],type(keepali0e[0])
lst2=[]
lst2.append(a)
print (id(lst2[0]),lst2[0],type(lst2[0]))
del a
print "--------------del a----------------"

print id(keepali0e[0]),keepali0e[0],type(keepali0e[0])
lst2.append(lst2[0])
print (id(lst2[0]),lst2[0],type(lst2[0]))

lst2.append(a)
print (id(lst2[0]),lst2[0],type(lst2[0]))

lst2.append(keepali0e[0])
print (id(lst2[0]),lst2[0],type(lst2[0]))
print (id(lst2[1]),lst2[1
