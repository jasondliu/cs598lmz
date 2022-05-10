from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
s.format = Struct.format
s.unpack = Struct.unpack
s.pack = Struct.pack

def read(file, offset, size):
	file.seek(offset)
	return file.read(size)

def read_struct(file, offset, struct):
	return struct.unpack(read(file, offset, struct.size))

def read_string(file, offset, length):
	return read(file, offset, length).decode('utf-8')

def read_uint8(file, offset):
	return read_struct(file, offset, s.pack('B'))[0]

def read_uint16(file, offset):
	return read_struct(file, offset, s.pack('H'))[0]

def read_uint32(file, offset):
	return read_struct(file, offset, s.pack('I'))[0]

def write(file, offset, data):
	file.seek(offset)
	file.write(data)

def write_
