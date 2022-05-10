from _struct import Struct
s = Struct.__new__(Struct)  # Create a new struct object without calling __init__
s.__init__('B')  # Initialize s
s.size  # Get size
s.pack('B', 0xFF)  # Start packing values
s.unpack('u', '\xff')  # Unpack/depack values


# Swapping bytes
x = 0xCCDD
x.to_bytes(2, byteorder = 'big')  # Bytes rep of x
x.to_bytes(2, byteorder = 'little')


# String format
print('Zeros and ones: {0:b}, {1:b}, {2:b}'.format(0, 1, -1))  # 0b1, ...
print('Introduce yourself: {name} {family}'.format(name = 'Bob', family = 'Doe'))


# Dictionaries
class FakeDict(dict):
   def __setitem__(self, key, value):  # __setitem__ overrides the set operation
       print('Setting...')  # We can do things in here
       return super().__setitem
