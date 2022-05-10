import bz2
# Test BZ2Decompressor

def read_bz2(fn):
    with bz2.open(fn, mode='rt', encoding='utf-8') as f:
        for l in f:
            yield l

with bz2.open('data/NC_014640.1.fa.bz2', mode='wt', encoding='utf-8') as f:
    f.write('2')

with bz2.open('data/NC_014640.1.fa.bz2', mode='rt', encoding='utf-8') as f:
    print(f.read())

# for l in bz2.BZ2File('data/NC_014640.1.fa.bz2'):
#     print(l)

# for l in read_bz2('data/NC_014640.1.fa.bz2'):
#     print(l)
# Test BZ2Compressor

def compress_bz2(fn):
    with open(fn, mode='rb') as f:
        with bz2.BZ2
