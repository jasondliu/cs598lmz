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

def illegal_operation():print "This operation is illegal."
from sys import intern
class c(object):
    def __getattribute__(self,name):
        if intern(name) in _forwarding:return super(c,self).__getattribute__(name)
        illegal_operation()
class _A(object):
    def _get_a(self):print 'getting A.a'
    a=property(_get_a)
_forwarding=[intern(i) for i in dir(_A)]
a=_A()
print a.a
b=c()
print b.a
"""

#p_mst.py
"""
import pymel.core as pm
from PySide import QtCore as qc
from PySide import QtGui as qg
from PySide import QtUiTools as qut
def getAngle(v1,v2):
    a,b=v1.normal().normal(),v2.normal().normal()
    theta=a.angle(b)*180/3.14
    cross=a.cross(b)
   
