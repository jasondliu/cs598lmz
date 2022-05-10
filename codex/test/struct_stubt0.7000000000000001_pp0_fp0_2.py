from _struct import Struct
s = Struct.__new__(Struct)

def get_sizeof_fmt(fmt):
	return s.size

def write_packet(packet, dst=sys.stdout):
	header_fmt = '>I'
	size = len(packet)
	header_size = get_sizeof_fmt(header_fmt)
	header = pack(header_fmt, size)
	dst.write(header)
	dst.write(packet)
	dst.flush()

def read_packet(src=sys.stdin):
	header_fmt = '>I'
	header_size = get_sizeof_fmt(header_fmt)
	header = src.read(header_size)
	size = unpack(header_fmt, header)[0]
	packet = src.read(size)
	return packet

def write_string(s, dst=sys.stdout):
	write_packet(s.encode(), dst)

def read_string(src=sys.stdin):
	packet = read_
