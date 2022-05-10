import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]='abc'
print(lst)
del a
print(lst)
#1.3.3.9 Weak Set
import weakref
class C(object):pass
c=C()
keepalive=[]
s=weakref.WeakSet()
s.add(c)
s.add(1)
s.add('abc')
keepalive.append(c)
keepalive.append(1)
keepalive.append('abc')
print(len(s))
print(s)
c=None
print(len(s))
print(s)
#1.3.3.10 Weak Key Dictionary
import weakref
class C(object):pass
c=C()
keepalive=[]
d=weakref.WeakKeyDictionary()
d[c]=123
d[(1,2,3)]=456
keepalive.append(c)
keepalive.append((1,2,3))
print(len(d))
print(d)
del c
print(len(d))
print
