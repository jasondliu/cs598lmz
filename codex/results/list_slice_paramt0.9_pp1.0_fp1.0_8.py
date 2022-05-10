import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
print a
#这里不能用print(lst[0])
print 'test'+str(lst[0])
a.d=a
a.e=a
a.f=a

del a   
#except print(lst[0])
print 'test'+str(lst[0])
