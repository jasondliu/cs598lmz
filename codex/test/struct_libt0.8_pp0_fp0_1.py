import _struct

PACK_FORMAT = 'B'

def vr_pack(value):
    return _struct.pack(PACK_FORMAT, value)

def vr_unpack(value):
    return _struct.unpack(PACK_FORMAT, value)[0]

def vr_unpack_str(value):
    return chr(vr_unpack(value))

VR_NAMES = dict(zip(
    ('AE', 'AS', 'AT', 'CS', 'DA', 'DS', 'DT', 'FD', 'FL', 'IS', 'LO', 'LT',
     'OB', 'OF', 'OW', 'PN', 'SH', 'SL', 'SQ', 'SS', 'ST', 'TM', 'UI', 'UL',
     'UN', 'US', 'UT'),
    range(28)
))

