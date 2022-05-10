import bz2
# Test BZ2Decompressor

try:
    content = bz2.BZ2Decompressor().decompress(zzbz2data)
except AttributeError as exc:
    print(exc)
else:
    print(content[0:100])

# compare with a regular BZIP2 decompression

with bz2.open(ifile, 'rb') as inf:
    content2 = inf.read()

print(content == content2)

print(hexlify(content[0:4]))
print(hexlify(content2[0:4]))

assert content == content2

'Extracting the original data'
'----------------------------------------------------------'

def extract_zstd(data):
    '''Extract the compressed meta data from the start of the
    compressed file'''

    meta_data = {}

    # reconstruct the crc32
    for name in ["content_size", "dict_id", "crc32"]:
        meta_data[name] =  int.from_bytes(data[:4], byteorder='little')
        data = data[
