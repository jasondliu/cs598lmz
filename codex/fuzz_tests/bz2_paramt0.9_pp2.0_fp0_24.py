from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(fileToDatabase(sys.argv[1]))
