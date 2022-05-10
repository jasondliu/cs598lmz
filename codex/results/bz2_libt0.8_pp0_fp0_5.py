import bz2
bz2.decompress(data)
 
def open_compressed(filepath, mode):
    if filepath.endswith('.bz2'):
        return bz2.open(filepath, mode)
    elif filepath.endswith('.gz'):
        return gzip.open(filepath, mode)
    else:
        return open(filepath, mode)

with open_compressed("data.csv", "w") as f:
    f.write("Writing to a compressed file")
!cat data.csv
with open_compressed("data.csv", "r") as f:
    print(f.read())
 
 
 
 
!cat data.csv.gz
 
from bz2 import compress, decompress
from base64 import b64encode, b64decode

original = b"this is the original text"
compressed = compress(original)
decompressed = decompress(compressed)

print("Original: %s" % original)
print("Compressed: %s" % b64encode(comp
