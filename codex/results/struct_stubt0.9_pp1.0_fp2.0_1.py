from _struct import Struct
s = Struct.__new__(Struct)
s.format = Struct.format.__get__(s, s)

def unpack(byts, p, l=1):
    r = [0] * l
    for i, sz in enumerate(s.format(p)):
        if sz == 'b':
            r[i] = byts[0]
            byts = byts[1:]
        elif sz == 'H':
            r[i] = (byts[0] << 8) + byts[1]
            byts = byts[2:]
        elif sz == 'L':
            r[i] = (byts[0] << 24) + (byts[1] << 16) + (byts[2] << 8) + byts[3]
            byts = byts[4:]
    return r

def parse_ev(buf_):
    byts = buf_[0:]
    ev = unpack(byts, 'HHLL')
    byts = byts[8:]
    extra = ev[2:]
    tv = mk
