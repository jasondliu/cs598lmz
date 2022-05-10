from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_XZ, memlimit=MEM_LIMIT)

# Tests instantiation of a decompressor with an invalid FORMAT
try:
	LZMADecompressor(format=FORMAT_AUTO + 1)
except ValueError:
	pass
else:
	print 'Error: expected ValueError'

# Try decompressing a bad XZ stream with FORMAT_AUTO
try:
	LZMADecompressor(format=FORMAT_AUTO).decompress('a' * 40)
except ValueError:
	pass
else:
	print 'Error: expected ValueError'

# Test memory limit
for format in (FORMAT_AUTO, FORMAT_XZ):
	dec = LZMADecompressor(format=format, memlimit=10 * 1024 * 1024)
	try:
		data = file(os.path.join(lzma_presets_dir, 'preset_uncomp’d_22.xz'), 'rb').read()
	except IOError, e:
		if e.errno
