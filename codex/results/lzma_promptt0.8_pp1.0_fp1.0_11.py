import lzma
# Test LZMADecompressor
comp = lzma.LZMADecompressor()
file = open('ooxml_sample.docx', 'rb')
content = file.read()
file.close()
result = comp.decompress(content)
print(result)

# Test LZMACompressor

comp = lzma.LZMACompressor()
file = open('docx_compressed.lzma', 'wb')
file.write(comp.compress(result))
file.close()

# Test CompressFile
test = lzma.compressfile(open('ooxml_sample.docx', 'rb'), format=lzma.FORMAT_ALONE)
print(test)

# Test DecompressFile
test = lzma.decompress(test)
print(test)

# Test open
file = lzma.open('docx_compressed.lzma', 'w')
file.write(b'Test')
file.close()

# Test is_check_supported
print(lzma.is_check_supported(
