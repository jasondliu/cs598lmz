import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
for i in range(10):
    print(lst)
    lst.append(str())
    lst.pop()
print(lst)
