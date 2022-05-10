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
print keepali0e[2:]#Return list containing [`Name`]
def func(n=0,lst=[]):
 lst.append(n)
 return lst
print func()#Return [0]
print func()#Return [0,0]
print func(1)#Return [0,0,1]
print func(2)#Return [0,0,1,2]
for i in range(0,3):func(i*3)
print func(1)#Return [0,0,1,2,0,3,6]
from scopetest import A
from scopetest import B
A.Scopetest()#Return Staticmember
from scopetest import A
B.Scopetest()#Return Boundmember
