import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#start
__name__="0"
class A(object):pass
def callback(x):import sys as s;s.exit(0)
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

import urllib.request
with urllib.request.urlopen('http://google.com') as response:
    html=response.read()

import urllib.request
with urllib.request.urlopen('http://exploitretailer.com/') as response:
    html=response.read
