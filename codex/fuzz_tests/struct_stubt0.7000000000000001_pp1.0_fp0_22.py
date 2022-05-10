from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hi')
len(s.pack(*xrange(1,4)))

# the above should not crash!
# this test was added because python 2.4.2 and earlier crash
