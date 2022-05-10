import lzma
lzma_preload = lzma.LZMADecompressor()
print(f'lzma.LZMADecompressor: {lzma_preload}')
print(f'lzma.LZMADecompressor.getstate: {lzma_preload.getstate()}')
print(f'lzma.LZMADecompressor.format_check: {lzma_preload.format_check(xz_data)}')
print(f'lzma.LZMADecompressor.decompress: {len(lzma_preload.decompress(xz_data))}')

import pylzma
lzma_preload = pylzma.decompressobj()
print(f'pylzma.decompressobj: {lzma_preload}')
print(f'pylzma.decompressobj.getstate: {lzma_preload.getstate()}')
print(f'pylzma.decompressobj.format_check
