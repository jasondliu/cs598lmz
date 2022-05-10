from bz2 import BZ2Decompressor
BZ2Decompressor


def read_raw_data(path, s=0, e=-1):
    with BZ2File(path) as f:
        data = f.read()
    if e < 0:
        e += len(data)
    return data[s:e]
