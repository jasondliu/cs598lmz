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

lst=[2, 3, 4]
for i in reversed(lst):print (i)
lst=[4, 5, 6]
for i in sorted(lst):print (i)
del i

import sys
sys.setrecursionlimit(1)
def func(x):func(x)
try:
    func('a')
except RuntimeError as ve:print (ve)
try:
    del lst[0]
except IndexError as e1:print (e1)


print ('ssssss'.replace('ss','ssssssss'))

print ('ss\r\ns\r\n'.replace('\r\n',' '))

print ('\u0480'.encode('utf-8').decode('utf-8'))

lst=[0, 1, 2, 3, 4, 5]
print (lst[0:1:-1])
print (lst[-5:4:1])
print (lst[2:4:2])
print (lst[::1])


print ('z' in 'abc
