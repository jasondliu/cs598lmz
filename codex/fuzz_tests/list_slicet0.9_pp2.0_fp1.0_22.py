import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print lst
```

```
def f():pass
def g():pass
def h():pass
o=type(f)
print o
```

```
class A(object):
def __init__(o self):
self.counter=0
def incr(o self):
self.counter+=1
class B(object):
def __init__(o self):
self.counter=0
def incr(o self):
self.counter+=IO
class C(A,B):
def incr(o self):
B.incr(self)
A.incr(self)
o=C()
o.incr()
print o.counter
```

```
x=tuple('abc')
print x

```

```
x=[dict(a=l,b=2,c=3)for l in range(1,4)]
y=2
z=3
print x
print filter(lambda d:d['b']==y and d['c']==z,x)
```

```

