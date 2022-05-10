from bz2 import BZ2Decompressor
BZ2Decompressor

try:
	n = int(sys.argv[1])
except IndexError:
	n = 1000

try:
	width = int(sys.argv[2])
except IndexError:
	width = 20
	
stream = BZ2Decompressor()

def decompress(n):
	count = 0
	for line in fileinput.input():
		count += 1
		yield stream.decompress(line)
		if count >= n:
			raise StopIteration
			
print '\n'.join(filter(None, (line.strip() for line in decompress(n))))
