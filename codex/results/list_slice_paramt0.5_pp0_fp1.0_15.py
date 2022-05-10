import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
gc.collect()
print(lst)

print(__name__)
print(__package__)
print(__file__)
print(__cached__)
print(__doc__)
print(__loader__)
print(__spec__)

from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))

from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

from collections import OrderedDict
d=dict
