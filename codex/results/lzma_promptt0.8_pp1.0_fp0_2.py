import lzma
# Test LZMADecompressor.
assert lzma.decompress(lzma.compress(b"xyz")) == b"xyz"
# Test LZMACompressor.
c = lzma.LZMACompressor()
assert c.compress(b"xyz") == b""
assert c.flush() == lzma.compress(b"xyz")
# Test LZMADecompressor.
d = lzma.LZMADecompressor()
assert d.decompress(lzma.compress(b"xyz")) == b"xyz"
print(d.eof)
assert d.decompress(b"") == b""
assert d.flush() == b""
print(d.eof)

xml_data = urllib.request.urlopen('http://www.w3schools.com/xml/cd_catalog.xml').read()
print(type(xml_data))

xml_file = open('cd_catalog.xml', 'wb')
xml_file.write(xml_data)
xml_file.
