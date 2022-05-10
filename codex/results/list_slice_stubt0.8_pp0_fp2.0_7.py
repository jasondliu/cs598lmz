import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst[0]=a
#del a
#del a.c
print 'a=',a
print 'a.c=',a.c
print 'lst[0]=',lst[0]
print 'id(a)=',id(a)
print 'id(a.c)=',id(a.c)
print 'id(lst[0])=',id(lst[0])
print 'id(a)==id(a.c)==id(lst[0])',id(a)==id(a.c)==id(lst[0])
print 'a==a.c==lst[0]',a==a.c==lst[0]
a.c=None
#del a
#del a.c
print 'id(a)=',id(a)
print 'id(a.c)=',id(a.c)
print 'id(lst[0])=',id(lst[0])
print 'id(a
