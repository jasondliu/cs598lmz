import bz2
# Test BZ2Decompressor on one file

file_name = "data/00.bz2"

with bz2.BZ2File(file_name) as file, \
        open("data/00.decompressed", "wb") as out_file:
    decompressor = bz2.BZ2Decompressor()
    for data in iter(lambda: file.read(100 * 1024), b''):
        out_file.write(decompressor.decompress(data))

# Test BZ2Decompressor on multiple files

file_names = ["data/{:02d}.bz2".format(i) for i in range(10)]

with open("data/all.decompressed", "wb") as out_file:
    for file_name in file_names:
        with bz2.BZ2File(file_name) as file:
            decompressor = bz2.BZ2Decompressor()
            for data in iter(lambda: file.read(100 * 1024), b''):
                out_file.write(decompressor.decompress
