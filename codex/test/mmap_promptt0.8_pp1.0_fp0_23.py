import mmap
# Test mmap.mmap

# Fails in mmap.mmap()
#    if len(buf) != len(data):
#       raise ValueError, "write length and data length must match"
#   ValueError: write length and data length must match
#
# 
# import mmap
#
# with open('test.bin', 'wb') as f:
#     f.write(b'\x01\x03\x00\xff')
#
# with open('test.bin', 'r+b') as f:
#     map = mmap.mmap(f.fileno(), 0)
#     map.seek(1)
#     map.write(b'23')

with open('test.bin', 'wb') as f:
     f.write(b'\x01\x03\x00\xff')
with open('test.bin', 'r+b') as f:
    map = mmap.mmap(f.fileno(), 0)
    map.seek(1)
    map.write_byte(b'\x32')
