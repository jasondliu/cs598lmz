import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

try:
    print(decompressor.decompress(b'BZh91AY&SY'))
    print(decompressor.decompress(b'BZh91AY&SY').decode())
except EOFError:
    print('EOFError')

try:
    print(decompressor.decompress(b'BZh91AY&SY').decode())
except EOFError:
    print('EOFError')

try:
    print(decompressor.decompress(b'BZh91AY&SYA'))
    print(decompressor.decompress(b'BZh91AY&SYA').decode())
except EOFError:
    print('EOFError')

try:
    print(decompressor.decompress(b'BZh91AY&SYA').decode())
except EOFError:
    print('EOFError')

try:
    print(decompressor.decompress(b'B
