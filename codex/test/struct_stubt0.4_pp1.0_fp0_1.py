from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

t = Struct('i?f')
t.size

import time
t0 = time.clock()
for i in range(1000000):
    x = Struct('i?f')
t1 = time.clock()
print('%.2f' % (t1-t0))

t0 = time.clock()
for i in range(1000000):
    x = Struct('i?f')
t1 = time.clock()
print('%.2f' % (t1-t0))

t0 = time.clock()
for i in range(1000000):
    x = Struct('i?f')
t1 = time.clock()
print('%.2f' % (t1-t0))

import time
t0 = time.clock()
for i in range(1000000):
    x = Struct('i?f')
t1 = time.clock()
print('%.2f' % (t1-t0))

t0 = time.clock()
