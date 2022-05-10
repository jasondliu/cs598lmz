import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
for obj in keepalive:
    print obj
print 'Before:',lst

lst[0]='spam'
for obj in keepalive:
    print obj
print 'After:',lst

a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
for obj in keepalive:
    print obj
print 'Before:',lst

lst[0]='spam'
for obj in keepalive:
    print obj
print 'After:',lst
