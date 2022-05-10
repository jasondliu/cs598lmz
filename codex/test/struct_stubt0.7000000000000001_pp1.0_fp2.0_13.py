from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')

t1 = time.time()
for i in range(10000000):
    s.pack(0)

t2 = time.time()
print('time1: ', t2-t1)

t1 = time.time()
for i in range(10000000):
    struct.pack('<h', 0)

t2 = time.time()
print('time2: ', t2-t1)

t1 = time.time()
for i in range(10000000):
    struct.Struct('<h').pack(0)

t2 = time.time()
print('time3: ', t2-t1)

t1 = time.time()
s = struct.Struct('<h')
for i in range(10000000):
    s.pack(0)

t2 = time.time()
print('time4: ', t2-t1)
'''

###############################################################################
'''
