from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = 0x4

def p(x):
    print(hex(x))

#p(0x8048320)

#p(0x8048370)

p(0x80483d0)

p(0x80484d0)

p(0x80485f0)
