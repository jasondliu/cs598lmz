import bz2
# Test BZ2Decompressor on a file
input_file = bz2.BZ2File('../data/output_kmers_1015.txt.bz2', 'rb')
# While in iterating mode, this file
# should produce lines from the original file
output_file = open('../data/test/kmers_1015.txt', 'w')
decompressor = bz2.BZ2Decompressor()
for data in iter(lambda: input_file.read(100 * 1024), b''):
    output_file.write(decompressor.decompress(data))
output_file.close()
input_file.close()


 
# Now test on an actual data set
data_dir = '../data/'
files = glob.glob(data_dir + '*.txt.bz2')
# Iterate using a generator expression (like a list comprehension but returns an iterator)
for filename in files:
    # Test on Kmers
    # https://docs.python.org/2/library/os.path.html
    input_file = bz2.BZ2File(
