import lzma
lzma_compressor = lzma.LZMACompressor()
print(lzma_compressor.compress(b'xyxxyxyxyxyxy'))
print(lzma_compressor.compress(b'xyxxyxyxyxyxy'))
print(lzma_compressor.compress(b'xyxxyxyxyxyxy'))
print(lzma_compressor.flush())

#lzma.open และ .xz
import lzma

with lzma.open('d:\\user\\desktop\\compress.xz', 'rb') as f:
    file_content = f.read()
print(file_content)

#lzma.LZMADecompressor
import lzma

decompressor = lzma.LZMADecompressor()
compressed = lzma.compress(b'xyxxyxyxyxyxy')
print(compressed)
#b'\xfd\x37\xb5\x05\x00\x00\x
