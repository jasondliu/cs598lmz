import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del keepali0e
#del a
print(lst)
#print(gc.collect())
print(lst)
print('a' in locals())
print(lst)
print('a' in locals())
#print(gc.collect())
print(lst)
print('a' in locals())
#print(gc.collect())
print(lst)
print('a' in locals())
#print(gc.collect())
print(lst)
print('a' in locals())
#print(gc.collect())
print(lst)
print('a' in locals())
#print(gc.collect())
print(lst)
print('a' in locals())
#print(gc.collect())
print(lst)
print('a' in locals())
#print(gc.collect())
print(lst)
print('a' in locals())
#print(gc.collect())
print(lst)
print('a' in locals())
#print(gc.collect())
print(lst)
print('a' in locals())

