from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode(), 2.7)

s.unpack(_)

s.unpack_from(bytes, 4)

import array
a = array.array('i', range(5))
a

import numpy as np
np.arange(5)

np.arange(5) + np.arange(5)

np.arange(5) + np.ones(5)

np.zeros(5)

np.ones(5)

np.ones((5, 5))

np.zeros((5, 5))

np.eye(5)

np.eye(5)[::-1]

np.diag(np.arange(5))

np.random.rand(5)

np.random.rand(4, 4)

np.random.randn(5)

np.random.randn(4, 4)

np.random.randint(5)

np.
