from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#bz2.decompress(data)

#print(len(data))

#print(data[:100].decode())

#http://stackoverflow.com/questions/10621711/how-to-calculate-the-md5-hash-of-a-large-file-in-python
import hashlib
import os
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

print(md5(os.path.join(os.path.dirname(__file__), 'data.bz2')))
