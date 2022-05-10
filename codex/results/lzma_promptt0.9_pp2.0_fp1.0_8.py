import lzma
# Test LZMADecompressor()
# 'x' mode is required in order to force writing the file in binary
f_lzma = open("data/sample.txt.xz", "rb")
lzma_decompressor = lzma.LZMADecompressor()
file_content = lzma_decompressor.decompress(f_lzma.read())
# Decode to ensure that string is in a readable format
file_content = file_content.decode('utf-8')

# Save the decompressed data
filename, file_extension = os.path.splitext("data/sample.txt.xz")
new_filename = filename + "_decompressed"
f_decompressed = open(new_filename, "w")
f_decompressed.write(file_content)
f_decompressed.close()

# Close the file handle
f_lzma.close()
import bz2
# Test BZ2Decompressor()
f_bz2 = open("data/sample.txt.bz2", "rb")
data = f_b
