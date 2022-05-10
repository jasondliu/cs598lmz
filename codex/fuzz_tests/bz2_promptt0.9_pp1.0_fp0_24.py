import bz2
# Test BZ2Decompressor object
with bz2.open('test.bz2', 'rb') as fin, open('test', 'wb') as fout:
    decom = bz2.BZ2Decompressor()
    data = fin.read(10000)
    while data != b'':
        fout.write(decom.decompress(data))
        data = fin.read(10000)

# Test decompressor interruption
with bz2.open('test.bz2', 'rb') as fin, open('test', 'wb') as fout:
    decom = bz2.BZ2Decompressor()
    data = fin.read(10000)
    while data != b'':
        fout.write(decom.decompress(data))
        if random.random() < 0.2:
            decom = bz2.BZ2Decompressor()
        data = fin.read(10000)


£$ ffprobe test.mp3
ffprobe version N-89200-g0d6b830 Copyright (c) 2007-2017 the FFmpeg developers
  built
