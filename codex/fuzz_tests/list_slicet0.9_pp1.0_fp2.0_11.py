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

@author: will
"""
import sys,re
li=sys.argv[0]
lis=re.findall('[a-z]',li)
lis.sort()
li=''
for i in lis:
    li+=i
print li
