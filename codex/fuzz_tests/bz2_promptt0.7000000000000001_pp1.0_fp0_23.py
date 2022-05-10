import bz2
# Test BZ2Decompressor

crc = 0
with bz2.BZ2File('compressed.bz2') as input:
    with open('uncompressed.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(block)
            crc = zlib.crc32(block, crc) & 0xFFFFFFFF

print('Decompressed:', crc)

with open('uncompressed.txt', 'rb') as input:
  print('Stored CRC:  ', zlib.crc32(input.read()) & 0xFFFFFFFF)

# Sample output from my machine:
# Decompressed: 2993648996
# Stored CRC:   2993648996

crc = 0
with bz2.BZ2File('compressed.bz2') as input:
    decompressor = bz2.BZ2Decompressor()
    while True:
        block = input.read(1024)
        if not block:
            break
        uncompressed =
