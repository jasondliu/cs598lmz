import bz2
# Test BZ2Decompressor on sample text

# load text
# tarfile.open(name=None, mode='r', fileobj=None, buffering=0, *, encoding=None, errors=None, pax_headers=None, debug=False, errorlevel=0, **kwargs)[source]
bz_file = tarfile.open(name="samples.tar.bz2", mode="r:bz2")
sample_txt = bz_file.extractfile("samples/sample2.txt").read()
sample_txt

# create decompressor object
decompressor = bz2.BZ2Decompressor()

# decompress by chunks
chunk_size = 100
offset = 0
decompressed = b''


if len(sample_txt) // chunk_size == 0:
    decompressed += decompressor.decompress(sample_txt)
else:
    while offset < len(sample_txt):
        decompressed += decompressor.decompress(sample_txt[offset:offset+chunk_size])
        offset += chunk_size
# print(decompressed
