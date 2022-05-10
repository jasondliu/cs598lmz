from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('P', False)

for _ in xrange(int(raw_input())):
    a, b = map(int, raw_input().split())
    print(long(s.pack(a))) + long(s.pack(b))
