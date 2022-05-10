import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
lst[0]="1"
del lst
print (1)
"""

"""
import os
os.system("pause")
"""


"""
import os

a=1
b=2
c=3
a,b,c=c,a,b
print(a,b,c)
"""

"""
#第一题
def func1():
    a=[0,1,2,3,4,5,6,7,8,9]
    b=[i for i in a[1::2]]
    return b
a = func1()
print(a)
"""

"""
#第二题
def func2():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = [i for i in a[::2]]
    return b
a = func2()
print(a)
"""

"""
#第三题
def func3():
   
