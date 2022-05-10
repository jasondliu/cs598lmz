import lzma
lzma_compressor = lzma.LZMACompressor()
print(lzma_compressor.compress(b'xyxxyxyxyxyxy'))
print(lzma_compressor.compress(b'xyxxyxyxyxyxy'))
print(lzma_compressor.compress(b'xyxxyxyxyxyxy'))
print(lzma_compressor.flush())

#lzma.open และ .xz
import lzma

