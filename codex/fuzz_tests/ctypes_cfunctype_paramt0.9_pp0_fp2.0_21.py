import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_char_p)
funci = FUNTYPE(calli)
cnt = 0
h = 0.0
s = struct.Struct('f')
bits = s.pack(h)
while True:
    '''
    if cnt < 20:
        print("cnt = {0}".format(cnt))
        print("bits = {0}".fmt(bits))
        cnt += 1
    '''
    h += 0.01
    if h >= 1.01:
        break
    bits = s.pack(h)
    print("bytes in bits: " + ":".join("{:02x}".format(ord(c)) for c in bits))
    print("{0}".format(funci(bits)))
