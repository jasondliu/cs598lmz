import bz2
# Test BZ2Decompressor
with bz2.open('../data/multiple-channels.mbox.bz2') as compressed:
    with open('../tmp/multiple-channels.mbox', 'wb') as f:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda: compressed.read(100 * 1024), b''):
            f.write(decompressor.decompress(data))
# Test BZ2File
with bz2.open('../data/single-channel.mbox.bz2', 'rb') as compressed:
    with open('../tmp/single-channel.mbox', 'w') as f:
        for line in compressed:
            f.write(line)
 
# Test tarfile
with tarfile.open('../data/multiple-channels.mbox.tar.bz2') as tar:
    tar.extractall('../tmp/multiple-channels/')
with tarfile.open('../data/single-channel.mbox.tar.bz2') as tar:
    tar.extractall('
