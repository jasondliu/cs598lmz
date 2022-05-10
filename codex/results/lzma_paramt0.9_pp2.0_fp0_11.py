from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from lzma import LZMADecompressor, FORMAT_AUTO
compressed_data = LZMADecompressor().compress(b'python')
decompressor = LZMADecompressor()
decompressed_data = b''
while True:
	chunk = decompressor.decompress(compressed_data)
	if chunk == b'':
		break
	decompressed_data += chunk
	
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from lzma import LZMADecompressor, FORMAT_AUTO
compressed_data = lzma.compress(b'python')
decompressor = LZMADecompressor(FORMAT_AUTO, None, None, 0, {'filter_id': lzma.FILTER_X86})
decompressed_data = decompressor.decompress(compressed_data)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import lzma

