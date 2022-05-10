import bz2
# Test BZ2Decompressor on data from the bytestring module.
decomp = bz2.BZ2Decompressor()
with bz2.open(os.path.join(os.path.dirname(__file__), 'bz2data.p.dat'), 'rb') as inp:
    data = inp.read()
    result = decomp.decompress(data, 8)
    result += decomp.flush()
    print(result)
