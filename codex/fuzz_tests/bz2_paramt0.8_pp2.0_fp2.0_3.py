from bz2 import BZ2Decompressor
BZ2Decompressor().decompress("".join([chr(i) for i in utils.get_input(9).read().split(",")]))

# Answer is 10704

# Part 2

BZ2Decompressor().flush()
