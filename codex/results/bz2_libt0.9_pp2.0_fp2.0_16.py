import bz2
bz2.test()


# using the with statement, which makes sure that the file is properly closed at the end, even if error occurs during accessing
from contextlib import closing

with closing(bz2.BZ2File('sample.bz2', 'wb')) as output:
	with open('sample.txt', 'rb') as input:
		output.write(input.read())


# decompressing data
import bz2

with open('sample.txt', 'rb') as input:
	data = input.read()

# compressing data
compressed = bz2.compress(data)
print(len(data))  # 98304
print(len(compressed))  # 6891
# as you can see, we're saving a lot of space by doing this

# writing compressed data to file
with open('sample.bz2', 'wb') as output:  # 'wb' indicates that we're writing in binary mode
	output.write(compressed)

print(bz2.decompress(compressed))


### Working with tar archives ###
'''
