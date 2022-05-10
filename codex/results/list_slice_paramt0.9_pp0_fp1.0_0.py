import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

del str
lst
lst=[]
attrs=['__module__','__doc__','__qualname__']
for x in attrs:
    keep=getattr(type,x)
    def calabel(x):
        def setter(self,value):
            keep=value
            print('setting...')
        del setter
    setattr(str,x,property(fget=lambda self:keep,fset=calabel(x)))
str.__module__='this'
str.__module__
str.__doc__
str.__quaname__='that'
str.__quaname__
from math import exp
from math import sin,cos
exp(1)
from math import exp as exponential
exponential(1)
from math import *
sin(0)
import math
math.exp(1)
import math as another_name
another_name.exp(1)
from math import *
from fractions import *
gcd(6,4)
from fractions import *
from math import *

