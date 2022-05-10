import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(a)
del a
del keepali0e
for i in range(100):
    lst.append(A())
    lst.append(A())
    lst.append((i,i))
    lst.append(A())
    lst.append(i)
    lst.append(str())
gc.collect()
lst[0]='123'
print(list(gc.get_referrers(lst[1])))
print(list(gc.get_referrers(lst[2])))
print(list(gc.get_referrers(lst[3])))
print(list(gc.get_referrers(lst[4])))
print(list(gc.get_referrers(lst[5])))
a=weakref.ref(lst,callback)

print('after:')
print(list(gc.get_referrers(lst[1])))
print(list(gc.get_referrers(lst[
