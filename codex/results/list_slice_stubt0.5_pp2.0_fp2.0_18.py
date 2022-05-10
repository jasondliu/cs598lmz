import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
lst.append(a)
lst.append(b)
keepalive=[]
keepalive.append(weakref.ref(a,callback))
keepalive.append(weakref.ref(b,callback))
print(lst)
del a
del b
print(lst)
gc.collect()
print(lst)

# 强引用
class A(object):
    pass
def callback(x):
    del lst[0]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
lst.append(a)
lst.append(b)
keepalive=[]
keepalive.append(a)
keepalive.append(b)
print(lst)
del a
del b
print(lst)
gc.collect()
print(lst)
