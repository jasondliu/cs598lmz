import lzma
# Test LZMADecompressor.read() blocks
for i in range(3):
	decompressor = LZMADecompressor()
	buf = b''
	for j in range(10):
		buf1 = decompressor.read(1)
		buf += buf1

		if buf1:
			continue

		if decompressor.eof:
			break
			
		buf2 = decompressor.unconsumed_tail
		decompressor.decompress(b'\x00')
		buf += buf2
	else:
		print('error in decompressor.read()')

	print('decompressor.read() blocks OK', i)

# Test LZMADecompressor.read1() blocks
decompressor = LZMADecompressor()
buf = b''
for j in range(10):
	try:
		buf1 = decompressor.read1(1)
	except EOFError:
		break
	else:
		print('error in decompressor.read1()')
		
	
