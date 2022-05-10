import lzma
# Test LZMADecompressor.

with lzma.open('blosum62.xz') as f:
	file_content = f.read()

file_content.split()[6]
print(file_content)
