import bz2
# Test BZ2Decompressor for data corruption

filename = 'Moby-Dick.txt.bz2'
filename2 = 'Moby-Dick.txt'

# with bz2.open(filename, 'rb') as input:
#     with open(filename2, 'wb') as output:
#         try:
#             output.write(input.read())
#         except IOError as e:
#             print(e)

