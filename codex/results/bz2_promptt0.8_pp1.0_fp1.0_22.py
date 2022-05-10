import bz2
# Test BZ2Decompressor to read bzip2 compressed stream in chunks
with bz2.open('data/sample_data/sample.bz2') as bz2file:
    decompress = bz2.BZ2Decompressor()
    for chunk in iter(lambda: bz2file.read(100), b''):
        data = decompress.decompress(chunk)
        if data:
            print(data)

#%%
# Test BZ2Decompressor to read bzip2 compressed stream in blocks
with bz2.open('data/sample_data/sample.bz2') as bz2file:
    decompress = bz2.BZ2Decompressor()
    while True:
            block = bz2file.read(1024)
            if not block:
                break
            data = decompress.decompress(block)
            if data:
                print(data)


#%%
# Test BZ2Decompressor to read bzip2 compressed stream in blocks
with bz2.open('data/sample_data/sample.bz2') as b
