import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst
d={}
e=[]
e.append(weakref.ref(d))
f=()
f+=(1,)
print f
d={1:'1',2:'2',3:'3'}
print d[1]
k=1
print k in d
d[1]='11'
print d
del d[1]
print d
d[1]='1'
del d[1]
print d
del d[2]
print d
d.clear()
print d

a={1:'1',2:'2'}
for k,v in a.items():
    print str(k)+'='+v
b=a.copy()
print b
for k,v in a.iteritems():
    print str(k)+'='+v

import bisect
a=[1,2,3,4]
print a
x=4
bisect.insort_left(a,x)
print a
x=6
bisect.insort_left(a,x)
print
