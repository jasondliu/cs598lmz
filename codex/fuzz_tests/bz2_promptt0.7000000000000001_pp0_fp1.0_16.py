import bz2
# Test BZ2Decompressor

with open('/home/ubuntu/cs230/datasets/bert/train.tsv.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('/home/ubuntu/cs230/datasets/bert/train.tsv.bz2.output', 'wb') as g:
        data = f.read(100)
        while data:
            g.write(decompressor.decompress(data))
            data = f.read(100)
import gzip
# Test gzip compressor

with open('/home/ubuntu/cs230/datasets/bert/train.tsv', 'rb') as f:
    with gzip.open('/home/ubuntu/cs230/datasets/bert/train.tsv.gz', 'wb') as g:
        g.writelines(f)
# Test gzip decompressor

with gzip.open('/home/ubuntu/cs230/datasets/bert/train.tsv.gz', 'rb') as f:
    with
