import lzma
# Test LZMADecompressor
comp = lzma.LZMADecompressor()
result = comp.decompress(b'\x00')  # raises EOFError
if result:
    print(result)

# using a loop, decompress will return the empty string when it is done:
comp = lzma.LZMADecompressor()
result = b''
chunk = b'\x00'
while chunk:
    try:
        result += comp.decompress(chunk)
        chunk = b''
    except lzma.LZMAError: # iterable needed in Python 3.0–3.1
        chunk = comp.unused_data

# 参考：http://blog.csdn.net/kenden23/article/details/15783321


import lzma
#
# model = lzma.LZMA_PRESET_DEFAULT
# level = 6
# fname1 = 'some_file'
# fname2 = 'some_file.xz'
#
# in_file = open(f
