import lzma
lzma.LZMAFile(filename)

with lzma.open(filename) as lzma_obj:
	print(lzma_obj.read())

with lzma.open(filename, mode="wt") as lzma_obj:
	lzma_obj.write("test test test test\n")

with lzma.open(filename) as lzma_obj:
	print(lzma_obj.read())

##############
# xz file
# python -m lzma test.xz
# xz test.txt
# xz -d test.xz
###############
import lzma
lzma.LZMAFile(filename)

with lzma.open(filename) as lzma_obj:
	print(lzma_obj.read())

with lzma.open(filename, mode="wt") as lzma_obj:
	lzma_obj.write("test test test test\n")

with lzma.open(filename) as lzma_obj:
