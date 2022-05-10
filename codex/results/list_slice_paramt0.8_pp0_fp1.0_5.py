import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print('before del lst:',lst)
del lst[0]
print('after del lst:',lst)


a_set=set([1,2,3,4])
frozenset([1,1,1,1])
frozenset([1,1,1,1],2)

from array import array
a=array('H',[1,2,3,4])
from collections import namedtuple
Person=namedtuple('Person','name age gender')
p=Person('maggie','28','F')
print(p,p.age,p.name)

from collections import deque
dq=deque(range(10),maxlen=10)
dq.rotate(3)
dq.rotate(-4)
dq.appendleft(-1)
dq.extend([11,22,33])
dq.extendleft([10,20,30,40])

from collections import defaultdict
dd=defaultdict(list)
dd['f'].append('maggie')
print(
