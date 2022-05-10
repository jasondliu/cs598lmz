from _struct import Struct
s = Struct.__new__(Struct)
print 'Compiled', s.size


# When a new Struct() is created, the class computes the sizes of all the fields (8 bytes)
# and the total size of the structure (16 bytes), producing
# the format string, which is now available as the class variable
print [field for field in dir(s)
           if not field.startswith('__')]
print s.format
