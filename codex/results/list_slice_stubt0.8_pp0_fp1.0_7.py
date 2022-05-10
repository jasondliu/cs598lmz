import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
keepalive.append(a.c)
lst[0]='_'
weakref.finalize(a, callback, lst)
dct={}
dct['_']=dct
dct=dct.copy()
for i in range(10):
    dct[str(i)]=dct
    dct=dct.copy()
"
