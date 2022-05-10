from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(savedcomp)

# GZIP
import gzip
compressor = gzip.GzipFile(fileobj = StringIO(savedcomp))
compressor.read()

# Pickle
import pickle
picklecomp = pickle.dumps(data)
pickle.loads(picklecomp)
