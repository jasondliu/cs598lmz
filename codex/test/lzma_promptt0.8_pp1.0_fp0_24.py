import lzma
# Test LZMADecompressor

with open("sample.xz", "rb") as in_file:
	with open("sample.txt", "wb") as out_file:
		xz_in = lzma.LZMADecompressor()
				
		in_data = in_file.read()
		out_data = xz_in.decompress(in_data)
				
		out_file.write(out_data)

 
# Packing and unpacking data

# http://pymotw.com/2/struct/

# http://pymotw.com/2/struct/index.html#module-struct

# http://docs.python.org/3/library/struct.html

# The struct module includes functions for converting between strings of bytes and native Python data types such as numbers and strings.

# Code:

import struct

data = '\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'


