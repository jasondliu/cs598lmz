import bz2
# Test BZ2Decompressor with an incorrect value for the "length" argument.
decompressor = bz2.BZ2Decompressor()
try:
    data = decompressor.decompress(b'BZh91AY&SY', 0)
except ValueError as err:
    print('Got expected exception:', err)


# Test BZ2Decompress.reset().
initial_state = decompressor.unused_data
decompressor.decompress(b'BZh91AY&SY', 0)
decompressor.reset()
assert initial_state == decompressor.unused_data
assert len(decompressor.unused_data) == 0
