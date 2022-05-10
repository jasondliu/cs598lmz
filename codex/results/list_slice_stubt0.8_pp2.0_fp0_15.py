import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.lst=lst
b=A()
b.c=a
b.lst=lst
lst.append(b)
lst.append(a)
lst.append(a)
lst.append(a)
del a
del b
print(lst)

print(gc.collect())
print(len(gc.get_referrers(lst)))
print(lst)
