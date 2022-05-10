import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive.append(a)
keepalive.append(a.b)
keepalive.append(a.b.c)
del a,a.b,a.b.c
callback('1')
del lst
del keepalive
del callback
```

```
#Python example
a=[]
a+=a
```

```
#Indexing
a = [0, 1, 2]
a[-1]      #= 2
a[-3]      #= 0
a[-3:-1]   #= [0, 1]
a[-3:-2]   #= [0]
a[-3:-3]   #= []
a[-3:-4]   #= []
a[-4:-3]   #= [0]
a[-5:-5]   #= []
a[-4:-4]   #= []
a[-4:-5]   #= []
a[-5:-4]   #= [0]
a[-5:-6]
