import lzma
lzma.open

def readFile(fname):
	b = None
	with open(fname, 'rb') as f:
		b = f.read()
	return b

def writeFile(fname, b):
	with open(fname, 'wb') as f:
		f.write(b)

def printHeader(b):
	print(b[0:3].decode('utf-8'))
	print(b[3:8].hex())
	print(b[8:12].hex())
	print(b[12:14].hex())

def main():
	if len(sys.argv) > 1:
		# if we have more than one argument, we should be able to open the file and extract the contents.
		b = readFile(sys.argv[1])
		printHeader(b)

