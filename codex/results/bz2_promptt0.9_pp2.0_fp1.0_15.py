import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
with open('data/dump.rdb', 'rb') as f:
    while True:
        compressed_data = f.read(1024)
        if len(compressed_data) == 0:
            break
        data = d.decompress(compressed_data)
        if data:
            print(data.decode())

## pair of bytes, first byte is indicator type, the second byte is a payload
# two bytes for length of string to follow
# length of string
# pair of bytes, first byte is indicator type, the second byte is a payload
# more length of string to follow
# length of string
# more strings...
# pair of bytes, first byte is indicator type, the second byte is a payload
# length of set to follow
# length of list of set members
# pairs of bytes for each set member
# pair of bytes, first byte is indicator type, the second byte is a payload
# length of list to follow
# length of list of list members
# pairs of bytes for each list
# more types...
# pair of bytes
