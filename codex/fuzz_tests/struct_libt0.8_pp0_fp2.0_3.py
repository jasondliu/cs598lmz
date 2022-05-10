import _struct

class tcp_hdr(pypacker.Packet):
	__hdr__ = (
		("src_port", "H", 0xdead),
		("dst_port", "H", 0xbeef),
		("seq_id", "I", 0xdeadbeef),
		("ack_id", "I", 0),
		("data_offset", "B", 0x50),
		("flags", "B", 0x02),
		("window_size", "H", 0x1234),
		("checksum", "H", 0),
		("urgptr", "H", 0)
	)

	# def bin(self):
	# 	print "bin"
	# 	return self.pack_hdr() + self.body_bytes

	def _update_fields(self):
		# set reserved bits to 0
		self.data_offset = (self.data_offset & ~0xf0) | (self.data_offset & 0xf0)
		# set checksum to 0
	
