from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open(sys.argv[1]).read())
