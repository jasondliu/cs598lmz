import _struct
# Test _struct.Struct(_struct.sizeof(_struct.calcsize(s)))
#
# CREATED:  7 Mar 2011
# MODIFIED: 7 Mar 2011


import _struct

s = ''.join([_struct.pack('HH', sn, sn) for sn in range(2**16)])
print(_struct.calcsize(s))
print(len(s))
print()

print(_struct.calcsize('HIH'))
print(_struct.sizeof(_struct.calcsize('HIH')))
print()

print(_struct.calcsize('9s2IH'))
print(_struct.sizeof(_struct.calcsize('9s2IH')))
print()

print(_struct.calcsize('2I2c5s'))
print(_struct.sizeof(_struct.calcsize('2I2c5s')))
print()

#print(_struct.calcsize('2I2c5s'))
#print(_struct.sizeof(_struct.calcsize('2I2c5s')))
#print()

#
