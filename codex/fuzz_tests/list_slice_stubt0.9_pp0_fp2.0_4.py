import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive=[]
for i in range(3):
keepalive=[StrongRef(a,callback)]
try:
print('A'*10000)
del keepalive
except TypeError:
pass
else:
print('If your python was not built --with-pydebug, this should have raised a TypeError')
keepalive=[]
for i in range(3):
keepalive=[StrongRef(a,keepalive)]
del keepalive
print('Done')
