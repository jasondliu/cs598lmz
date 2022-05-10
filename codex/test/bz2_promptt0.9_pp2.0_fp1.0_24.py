import bz2
# Test BZ2Decompressor:


def BZ2file(filename):
    fileobj = open(filename, "rb")
    decomp = bz2.BZ2Decompressor()
    results = ""
    d = fileobj.readline()
    while d:
        results += decomp.decompress(d)
        d = fileobj.readline()
    fileobj.close()
    return results
