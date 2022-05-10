import lzma
lzma.LZMADecompressor().decompress(bytes(lzma_dumped)).decode("utf-8")

from zlib import decompress
decompress(bytes(zlib_pipelined))
decompress(bytes(zlib_dumped))

# No success pulling the svg and color mappings out of the first compressed bit
from zlib import decompress
from bz2 import decompress
from lzma import LZMADecompressor
from zlib import decompress
decompress(disassembly_chunk, wbits=-MAX_WBITS)
lzma_in = LZMADecompressor().decompress(disassembly_chunk)
bz2_in = decompress(lzma_in)
bz2_in
decompress(bz2_in)
summary_chunk
def process_chunk(chunk):
    return decompress(chunk, wbits=-MAX_WBITS)
chunk = summary_chunk
decompress(chunk)
summary_chunk = decompress(
