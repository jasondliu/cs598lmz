import lzma
# Test LZMADecompressor

data = b'this is the data to compress'

compressor = lzma.LZMACompressor()
comp_data = compressor.compress(data)
comp_data += compressor.flush()

decompressor = lzma.LZMADecompressor()
decomp_data = decompressor.decompress(comp_data)

print(decomp_data)

compressor = lzma.LZMACompressor(format=lzma.FORMAT_RAW, filters=[
    {"id": lzma.FILTER_X86, "preset": 3},
    {"id": lzma.FILTER_LZMA2, "preset": 3},
    ])
with open("foo.xz", "wb") as out:
    out.write(compressor.compress(data))
    out.write(compressor.flush())
name = "historical.json"
name1 = "historical-predictions.json"
import json
import os

def read_json_file(json_name):
    with open("../../
