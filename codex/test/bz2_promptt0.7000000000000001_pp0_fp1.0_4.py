import bz2
# Test BZ2Decompressor

def read_bz2(fn):
    with bz2.open(fn, mode='rt', encoding='utf-8') as f:
        for l in f:
            yield l

