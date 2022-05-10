import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
print('a=%r,lst=%r,keepalive=%r'%(a,lst,keepalive))
del a
#这是形成"循环引用"
a=A()
weakref.ref(lst,callback)
print('strong站:',gc.collect())
#del a
print('strong站:',gc.collect())
print('a=%r,lst=%r,keepalive=%r'%(a,lst,keepalive))
