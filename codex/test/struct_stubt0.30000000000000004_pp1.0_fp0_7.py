from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# pack
s.pack(1, b'ab', 2.7)

# unpack
s.unpack(_)

# pack_into
buffer = bytearray(s.size)
s.pack_into(buffer, 0, 1, b'ab', 2.7)

# unpack_from
s.unpack_from(buffer, 0)

# format
s.format('<', 'I 2s f')

# calcsize
s.calcsize('I 2s f')

# Struct instances are immutable
s.format = 'I 2s f'
s.format

# Struct instances are hashable
hash(s)

# Struct instances are picklable
import pickle
pickle.dumps(s)

# Struct instances are copyable
import copy
copy.copy(s)

# Struct instances are deepcopyable
copy.deepcopy(s)

# Struct instances have a readable repr
repr(s)

# Struct instances have a readable
