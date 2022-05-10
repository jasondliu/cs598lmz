from _struct import Struct
s = Struct.__new__(Struct)
s.struct = Struct('i?')
s.parse = s.struct.unpack_from
PCSLOT_DATA_EMPTY = {}
pcslot_empty_struct = Struct('3H')
PCSLOT_DATA_EMPTY['pcslot_empty'] = pcslot_empty_struct.size
PMSLOT_DATA_EMPTY = {}
pmslot_empty_struct = Struct('I')
PMSLOT_DATA_EMPTY['pmslot_empty'] = pmslot_empty_struct.size
SHAREDPVPSLOT_DATA_EMPTY = {}
sharedpvpslot_empty_struct = Struct('3B3H2B')
SHAREDPVPSLOT_DATA_EMPTY['sharedpvpslot_empty'] = sharedpvpslot_empty_struct.size
PERSISTENTSLOT_DATA_EMPTY = {}
persistentslot_empty_struct = Struct('4B')
PERSISTENTSLOT_DATA_EMPTY['persistentslot_empty'] = persistentslot_empty_struct.size
