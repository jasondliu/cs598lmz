from _struct import Struct
s = Struct.__new__(Struct)
print s
print s.unpack
print s.unpack("ssss")
print dir(s)
print s.__new__
print s.__init__
print type(s)

print
print "--------------------------------------------------------------------------------"
print "--------------------------------------------------------------------------------"


import time
print time.__dict__
print time.__module__

print
print "--------------------------------------------------------------------------------"
print "--------------------------------------------------------------------------------"

class Person:
    pass

print Person.__dict__
print Person.__name__
print Person.__module__

print
print "--------------------------------------------------------------------------------"
print "--------------------------------------------------------------------------------"

import sys
print sys
print sys.__name__
print sys.__doc__
print sys.__file__
print sys.__builtins__
print sys.__class__
print sys.__dict__
print sys.__module__
print sys.__doc__
print sys.__name__

print
print "--------------------------------------------------------------------------------"
print "--------------------------------------------------------------------------------"
