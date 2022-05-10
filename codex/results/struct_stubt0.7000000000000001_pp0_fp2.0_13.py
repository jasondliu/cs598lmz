from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>L')
for i in range(1000):
    s.pack(i)

print(time.perf_counter() - start)
