import lzma
# Test LZMADecompressor.
with lzma.open("example.xz") as f:
    file_content = f.read()
    print(file_content)
 
# Test LZMAFile with explicit LZMADecompressor.
compressor = lzma.LZMADecompressor()
with lzma.LZMAFile(f) as xz_file:
    file_content = xz_file.read()
    print(file_content)
