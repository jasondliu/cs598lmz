import gc, weakref
from nebula2 import *

low = pynebula.pyLoad("low.tga")
high = pynebula.pyLoad("high.tga")

def f(t): print t, " objects are left"

t = pynebula.pyText()
t.setobject("mystring")
t2 = pynebula.pyLoad("test.txt")
t3 = pynebula.pyText("abc")

r = pynebula.pyRawmesh()
r2 = pynebula.pyLoad("test.n3d2")
r3 = pynebula.pyRawmesh("test.n3d2")

s = pynebula.pyShape()
s2 = pynebula.pyLoad("test.n2")
s3 = pynebula.pyShape("test.n2")

t4 = pynebula.pyLoad("test.jpg")
t = None
t2 = None
t3 = None
t4 = None

s = None
s2 = None
s3
