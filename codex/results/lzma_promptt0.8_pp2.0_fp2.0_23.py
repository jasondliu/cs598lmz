import lzma
# Test LZMADecompressor()

BLOCKSIZE = 16 * 1024

decompressor = lzma.LZMADecompressor()

with open("data/python-3.7.0a2.tar.xz.part", "rb") as input:
    with open("python-3.7.0a2.tar", "wb") as output:
        while True:
            block = input.read(BLOCKSIZE)
            if not block:
                break
            output.write(decompressor.decompress(block))
options = {
    'format': 'xz',
    'level': 9,
    'check': lzma.CHECK_CRC64,
    'filters': [
        {'id': lzma.FILTER_LZMA2, 'preset': 9 | lzma.PRESET_EXTREME},
    ],
}

compressor = lzma.LZMACompressor(**options)

with open("data/python-3.7.0a2.tar", "rb") as input:
    with open("python-3
