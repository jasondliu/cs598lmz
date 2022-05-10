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

def data_load (data):
	return "".join("\\x%02x" % x for x in data)

class Server(object):

	# pylint: disable=too-many-arguments

	def __init__(self, address, port, user, password, db_name=None, use_unicode=True, charset="utf8",
				 connect_timeout=None, read_timeout=None, write_timeout=None,
				 no_delay=False, autocommit=False, client_flag=0, cursorclass=None):
		"""
		Create a new connection to
