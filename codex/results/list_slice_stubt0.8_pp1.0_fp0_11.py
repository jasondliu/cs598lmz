import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
sys.getrefcount(a)
a.b=weakref.ref(a)
print a.b.__class__
print(callback.__class__)
print(callback.__class__.__name__)
print(callback)
print(callback.__name__)

a=A()

a.x=weakref.ref(a,callback)
#del a.x
lst.append(a)

del a
sys.getrefcount(a)

for x in lst:
    print(x)
    if x==str():
        lst.remove(x)

lst.append(callback)

for x in lst:
    print(x.__class__)
    print(x.__class__.__name__)
    print(x)
    print(x.__name__)



print(a)

if a.b() is a:
    print('true')
else:
    print('false')

#del x
