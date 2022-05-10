import bz2
# Test BZ2Decompressor
input_file = bz2.BZ2File('sample.bz2')
data = input_file.read()
print(data)

# Difference between read and readlines
input_file.seek(0)
data = input_file.readlines()
print(data)
