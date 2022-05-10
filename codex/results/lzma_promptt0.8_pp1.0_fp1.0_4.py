import lzma
# Test LZMADecompressor

# from https://www.unicode.org/Public/UCD/latest/ucd/NormalizationTest.txt
with open("NormalizationTest.txt", "rb") as f:
    raw = f.read()

with lzma.open("compressed.lzma", "wb") as f:
    f.write(raw)

with lzma.open("compressed.lzma") as f:
    raw_dec = f.read()

with open("NormalizationTest_decompressed.txt", "wb") as f:
    f.write(raw_dec)

# compare the original file with the decompressed
result = raw == raw_dec
print("Decompression successful:", result)

os.remove("NormalizationTest_decompressed.txt")
os.remove("compressed.lzma")

# NormalizationTest.txt - 337.62KB
# compressed.lzma - 322.21KB
# NormalizationTest_decompressed.txt - 337.62KB

# compression rate: 95.59%

# Realistically
