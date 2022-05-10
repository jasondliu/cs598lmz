from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# decompress the data
decompressed_data = LZMADecompressor().decompress(compressed_data)

# display the decompressed data
decompressed_data

# convert the decompressed data into a string
decompressed_data.decode('utf-8')

# convert the data into a string and split it
election_data = decompressed_data.decode('utf-8').split()

# print the first 100000 words in the split data
print(election_data[:100000])

# import Counter from collections
from collections import Counter

# create a Counter object with the split data
bow = Counter(election_data)

# print the 10 most common words
print(bow.most_common(10))

# import counter and defaultdict
from collections
