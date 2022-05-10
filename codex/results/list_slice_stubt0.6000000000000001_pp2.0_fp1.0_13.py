import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(weakref.ref(lst,callback))
print('a,lst:',a,lst)
del a,lst
print('keepali0e:',keepali0e)
print('len(keepali0e):',len(keepali0e))
#a,lst: <__main__.A object at 0x000001E9E1716E80> ['']
#keepali0e: [<__main__.A object at 0x000001E9E1716E80>, <weakref at 0x000001E9E1716C48; to 'list' at 0x000001E9E1716B70>]
#len(keepali0e): 2
from heapq import *
h=[]
heappush(h,(5,'write code'))
heappush(h,(7,'release product'))
heappush(h,(1,'write spec'))
heappush(h,(3,'create tests'))
print('h:',h)
