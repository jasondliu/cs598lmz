import lzma
# Test LZMADecompressor
print("### Test LZMADecompressor ###")
print("---")
print("--- Test 1 ---")
lz = lzma.LZMADecompressor("")
print("--- Test 2 ---")
try:
	lz = lzma.LZMADecompressor("", {1: 2})
except:
	pass
print("--- Test 3 ---")
lz = lzma.LZMADecompressor("")
print("--- Test 4 ---")
lz.decompress("")
print("--- Test 5 ---")
lz.decompress("")
print("--- Test 6 ---")
lz.decompress("")
print("--- Test 7 ---")
lz.decompress("")
print("--- Test 8 ---")
lz.decompress("")
print("--- Test 9 ---")
lz.decompress("")
print("--- Test 10 ---")
lz.decompress("")
print("--- Test 11 ---")
lz.decompress("")
print("--- Test 12 ---")
lz
