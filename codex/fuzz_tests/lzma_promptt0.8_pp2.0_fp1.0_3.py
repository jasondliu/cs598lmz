import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
#inputLZMA = open("./lzmadec.in", "rb")
inputLZMA = open("./test/test.in", "rb")
outputLZMA = open("./test/test.out", "wb")
try:
	while True:
		chunk = inputLZMA.read(1024 * 1024)
		if len(chunk) == 0:
			break
		outputLZMA.write(lzc.decompress(chunk))
finally:
	outputLZMA.close()
	inputLZMA.close()
