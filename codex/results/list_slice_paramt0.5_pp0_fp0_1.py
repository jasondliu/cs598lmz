import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

def f(x):
    print(x)
    del lst[0]
    print(lst)
    lst.append(lst)
    print(lst)
lst=[1]
print(lst)
lst.append(lst)
print(lst)
