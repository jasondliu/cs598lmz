import bz2
# Test BZ2Decompressor on the first 10 rows of file
with open("/home/dks/test-virtualenv3/test-db/bz2/big_test_file.bz2","rb") as input:
    bz_comp = bz2.BZ2Decompressor()
    for i, line in enumerate(input):
        if i > 10: break
        print("Line: {}".format(bz_comp.decompress(line)))

print("\n")

# You can also use BZ2File as a context manager for ease of use
with bz2.BZ2File("/home/dks/test-virtualenv3/test-db/bz2/big_test_file.bz2", "rb") as input:
    bz_comp = bz2.BZ2Decompressor()
    for i, line in enumerate(input):
        if i > 10: break
        print("Line: {}".format(bz_comp.decompress(line)))

print("\n")


# Test BZ2File
with bz
