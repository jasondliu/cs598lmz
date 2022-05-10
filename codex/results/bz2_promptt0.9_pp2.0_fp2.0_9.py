import bz2
# Test BZ2Decompressor
dec = bz2.BZ2Decompressor()

# Decompress the compressed binary data from a file
# and write the output to `stdout`
with open('sample.bz2', 'rb') as infile:
	eof = False
	block_sz = 100
	while not eof:
		block = infile.read(block_sz)
		if len(block) < block_sz:
			eof = True
		out = dec.decompress(block)
		if out:
			sys.stdout.wri
