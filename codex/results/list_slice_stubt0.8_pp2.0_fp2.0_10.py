import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=1
dct={1:1,2:2}
for i in xrange(100000):
    dct[a]=1
    c=dct.pop(1)
    c=dct.pop(2)
    del dct[1],dct[2]
    dct.clear()
    dct={1:1,2:2}
    key1=(a,a,a)
    key2=(a,a,a)
    dct[key1]=1
    dct[key2]=2
    c=dct.pop(key1)
    c=dct.pop(key2)
    del dct[key1],dct[key2]
    dct.clear()
    dct={key1:1,key2:2}
    k1=weakref.ref(a,callback)
    k2=weakref.ref(a,callback)
    dct[k1]=1
    dct[k2]=2
    c=dct.pop(k1)
    c
