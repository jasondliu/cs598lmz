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
c=keepali0e[-2][0]
a=A()
a.c=a
bs=A()
bs.c=a
lst.append(str())
del bs #引用计数-1，但作为list中的元素也又重新引用了
del lst
print(a)
print(c)
#lst = [1, 2, 3]
#print(lst[:])
