import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
a.b=b
b.b=a
a.x=lst
b.x=lst
keepalive.append(a)
keepalive.append(b)
del a
del b
gc.collect()
s1=str(lst[0])
lst=[]
gc.collect()
s2=str(lst[0])
assert s1==s2=='[]'
lst[0]=weakref.ref(A(),callback)
gc.collect()
assert lst==[]
from test import test_support
with test_support.check_py3k_warnings(quiet=True):
	from UserList import UserList
from collections import deque
from copy import copy
list=list
from heapq import heapify
import random
from sys import getrefcount
from thread import start_new_thread
try:
	from threading import Thread,Lock
except ImportError:
	from dummy_threading import Thread,Lock
from types import XRangeType,StringType,IntType,LongType

