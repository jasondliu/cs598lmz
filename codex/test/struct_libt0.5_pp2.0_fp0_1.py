import _struct

def _bcd_to_int(bcd):
    return int(''.join([str((bcd >> 4) & 0x0F), str(bcd & 0x0F)]))

def _int_to_bcd(i):
    return int(''.join([str(i)[0], '0', str(i)[1]]))

