import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
#print(lst)
"""
class A(object):pass
a=A()
b=A()
a.s=b
c=A()
b.s=c
d=A()
c.s=d
d.s=a
keepali0e=[]
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a,callback))
def walk(ob,seen):
    li=ob.__dict__.items()
    for k,v in li:
        d=seen.get(id(v))
        if d is None:
            #print(k,v)
            seen[id(v)]=None
            walk(v,seen)
        #else:print("already seen %s %s"%(k,v))
def callback(x):
    ob=x()
    if ob is not None:
        print("callback",ob)
seen={id(A):None}
keepali0e.append(weakref.ref(C,callback
