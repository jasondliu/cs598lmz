import bz2
# Test BZ2Decompressor
#
# for i in range(10):
#     f = bz2.BZ2File('output/part-0000{}'.format(i))
#     try:
#         print(f.readline())
#     finally:
#         f.close()
 
# Test BZ2File
#with bz2.BZ2File('output/part-00000', 'rb') as f:
#     for line in f:
#         print(line)
#         break


# Test BZ2Compressor
# with open('output/part-00000', 'r') as f, bz2.open('output/part-00000.bz2', 'wt') as f_out:
#     f_out.write(f.read())

# Test BZ2File
