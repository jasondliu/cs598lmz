from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>QQQQQQQQQQQ'
s.size   = 88

try:
	from _struct import unpack_from
except ImportError:
	def unpack_from(f, off):
		f.seek(off)
		return s.unpack(f.read(s.size))

def unpack(f):
	return unpack_from(f, 0)

def pack(f, id0, id1, id2, id3, id4, id5, id6, id7, id8, id9, id10, id11):
	f.write(s.pack(id0, id1, id2, id3, id4, id5, id6, id7, id8, id9, id10, id11))

def gen_tlv(dict):
	f = StringIO()
