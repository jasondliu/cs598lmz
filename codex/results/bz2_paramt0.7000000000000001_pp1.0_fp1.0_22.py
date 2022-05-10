from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

data = BZ2Decompressor().decompress(compressed_data)

# The data is stored in compressed format (bz2)
# decompress data into a string
# data = bz2.decompress(compressed_data)

# data is a string, parse it as xml
xml = ElementTree.fromstring(data)

# total value of all counts
counts = xml.findall('.//count')
print('Counts: ', len(counts))

# sum of the numbers in the file
total = sum(int(count.text) for count in counts)
print('Total: ', total)
