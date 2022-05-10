import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
lst.append(a)
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
lst.append(a)
a.b=1
lst.append(a)
print(lst)
# print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])
