import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(a,callback))
del a
for test in range(100):lst[0]+=chr(65);del lst[0];lst.append(str)
del a
print(keepali0e[0](), keepali0e[1]())
</code>

