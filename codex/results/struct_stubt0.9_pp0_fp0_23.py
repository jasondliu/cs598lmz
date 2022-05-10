from _struct import Struct
s = Struct.__new__(Struct)

def pack(file, fmt, vals):
	f = open(file, "wb")
	data = s.pack(fmt, *vals)
	f.write(data)
	f.close()

def unpack(file, fmt):
	f = open(file, "rb")
	data = f.read()
	return s.unpack(fmt, data)

def disp(fmt, vals):
	buf = s.pack(fmt, *vals)
	for b in buf:
		c = b
		if c <= 0x20 or c >= 0x7f:
			c = ord(".")
		print("%c" % c, end="")
	print("")

print("="*78)

disp("12s",
	("\x00AaBbCcDdEe\x00\x00\x00",))

disp("!5sd5s",
	("\x03\x04\x05\x06\x07", "\x00AaB
