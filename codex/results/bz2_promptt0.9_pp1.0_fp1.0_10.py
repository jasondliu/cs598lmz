import bz2
# Test BZ2Decompressor - decompress data and return decoded strings

decompressor = bz2.BZ2Decompressor()
uncompressed_data = decompressor.decompress(compressed_data)

uncompressed_data

# The BZ2Decompressor class also provides an unfinished attribute, which is False when the end of the compressed data stream has been reached. 
# Once the stream has finished, any further call to the decompress() method will just return empty bytes objects.
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)
decompressor.unused_data

# A single decompressor object supports additional calls to the decompress() method to feed new compressed data to the object when not using a file:
decompressor = bz2.BZ2Decompressor()

while True:
	block = f.read(1024)
	if not block:
	    break
	decompressed = decompressor.decompress(block)
	if decompressed:
	    pass
	    # process(decompressed)

