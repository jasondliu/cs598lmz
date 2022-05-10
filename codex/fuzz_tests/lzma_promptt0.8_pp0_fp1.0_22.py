import lzma
# Test LZMADecompressor output
comp = lzma.LZMADecompressor()
with open("data/python-3.7.2.tar.xz", "rb") as file:
    data = file.read(1024)
    test = comp.decompress(data)
import lzma
# Test LZMADecompressor output
comp = lzma.LZMADecompressor()
with open("data/python-3.7.2.tar.xz", "rb") as file:
    data = file.read(1024)
    test = comp.decompress(data)
type(test)

with open("data/python-3.7.2.tar.xz", "rb") as file:
    data = file.read(1024)
    print(data)
    test = comp.decompress(data)
    print(test)
    print("Byte size of test:", sys.getsizeof(test))

with open("data/python-3.7.2.tar.xz", "rb") as file:
    data = file.
