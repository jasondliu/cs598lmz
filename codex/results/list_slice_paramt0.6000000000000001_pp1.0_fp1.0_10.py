import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print lst

#tuple
print 'tuple'
t=tuple()
print t,'len:',len(t)
t1=(1,)
t2=(1,2,3)
print t1,'len:',len(t1)
print t2,'len:',len(t2)
t3=tuple(range(10))
print t3,'len:',len(t3)
t4=tuple('abcdefghijklmnopqrstuvwxyz')
print t4,'len:',len(t4)
t5='abcdefghijklmnopqrstuvwxyz'
print t5,'len:',len(t5)
print t5[10:20:2]
print t4[10:20:2]
print 't4.index(j):',t4.index('j')
print 't4.index(j,10):',t4.index('j',10)
print 't4.index(j,10,20):',
