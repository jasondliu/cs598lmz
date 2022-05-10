import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=100
keepalive=[a,a.c,a.b,lst,A]
lst[0]=a
print 'lst:',lst
print 'lst[0].a:',lst[0].b
print 'lft[0].c:',lst[0].c
print 'lst[0].i:',lst[0].c.c.b
print 'lst[0].a:',lst[0].c.c.c.b
weakref.finalize(lst,callback)
del lst
print 'Finished'
