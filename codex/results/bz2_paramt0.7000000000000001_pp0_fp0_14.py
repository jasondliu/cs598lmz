from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("enwik8_decompressed.bz2", "wb"))

# with open("enwik8_decompressed.bz2", "wb") as new_file, bz2.BZ2File("enwik8.bz2", "rb") as file:
#     for data in iter(lambda : file.read(100 * 1024), b""):
#         new_file.write(data)


# import bz2
# import os
# os.system("bzip2 -dk enwik8.bz2")
# with bz2.BZ2File("enwik8.bz2", "rb") as bz2_file, open("enwik8_decompressed.bz2", "wb") as new_file:
#     for data in iter(lambda : bz2_file.read(100 * 1024), b""):
#         new_file.write(data)
