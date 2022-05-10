from _struct import Struct
s = Struct.__new__(Struct)
s.size = 8
s.format = "dd"
float_pair_struct = s
del s

def float_pair_pack (floats):
	return float_pair_struct.pack(*floats)

def float_pair_unpack (data):
	return float_pair_struct.unpack(data)

def data_dump (data):
	return "".join("%02x " % x for x in data)

