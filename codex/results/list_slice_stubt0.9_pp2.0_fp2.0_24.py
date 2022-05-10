import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a_wr=weakref.ref(a,callback)
obj_id=id(a)
keepaalive.append(a)
del a
a_wr
lst
keepaalive[0].c is keepaalive[0]
gc.collect()
lst
gc.collect()
lst

a.b=a
a_wr =weakref.ref(a,callback)
keepalive.append(a)
del a

print a_wr()

a_wr() is keepalive[0]
import puremvc
puremvc.__version__
"abc".join(['a','b','c'])

'abc'.capitalize()

filter(lamba i:i>0,[0,-1,1])

filter(lambda i: i>0,(0,-1,1))

map(lambda x,y:x+y,[1,2,3],[4,5,6])

filter(lambda x: x>0,(0,-1,1))

l=list(filter(lambda x: x
