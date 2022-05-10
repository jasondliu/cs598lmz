from _struct import Struct
s = Struct.__new__(Struct) # bug
s._repr_ = lambda: 'whatevs'
s = Struct('=I') # ok
s = Struct('=I')(10) # ok
t = Struct.__new__(Struct) # this use of __new__ prevents the magic methods
# This enables pickling, but disables the magic functions
print(s.csize)
hllapi()
