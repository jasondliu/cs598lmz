from lzma import LZMADecompressor
LZMADecompressor.decompress(b'\xfd\x37\x7a\x58\x5a\x00')

def decompress(data):
	return LZMADecompressor.decompress(data[:-2])

def parse_opcode(opcode):
	name = opcode
	if len(opcode) == 0:
		pass
	elif opcode[-1] in "0123456789":
		name = opcode[:-1]
		opcode = opcode[-1]
	else:
		opcode = ""
	return name,opcode

def parse_type(name):
	c = name[-1]
	if c not in "0123456789":
		return name
	name = name[:-1]
	if name in class_names:
		return name
	return name,c

def parse_raw_type(name):
	c = name[-1]
	if c not in "0123456789":
		return name
	return name[:-
