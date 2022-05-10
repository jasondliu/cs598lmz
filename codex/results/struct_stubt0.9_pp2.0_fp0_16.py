from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">iii"
d = s.unpack_from("hhhh", "foo")
print d
d2 = s.unpack_from("hhhh", "foo", 1)
print d2
# the following line would ordinarily create the exception:
#   ValueError: unpack str size does not match format
#d3 = s.unpack_from("hhhh", "foo", 2)

print "__doc__ =", s.__doc__
# the following line would ordinarily create the exception:
#   AttributeError: Struct instance has no attribute '__iter__'
#for i in s:
#  print i
print "format =", s.format
