from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(comp_data)

## 16. Multiple Compression Layers ################################

new_comp_data = BZ2Compressor().compress(
    BZ2Compressor().compress(comp_data)
)

with open("new_comp_data.bz2", "wb") as f:
    f.write(new_comp_data)

new_comp_decomp = BZ2Decompressor().decompress(
    BZ2Decompressor().decompress(new_comp_data)
)

comp_data == new_comp_decomp

## 17. Unbuffered Decompression ################################

class BZ2DecompressorEx(BZ2Decompressor):

    def decompress(self, data, size=12):
        return super().decompress(data, size)

## 18. How to Buffer Decompression ################################

d = zlib.decompressobj()
decompressed_data = d.decompress()

if b"hello" in decompressed
