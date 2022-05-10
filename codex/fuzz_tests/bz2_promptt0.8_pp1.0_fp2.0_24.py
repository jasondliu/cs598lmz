import bz2
# Test BZ2Decompressor
bz_decompressor = bz2.BZ2Decompressor()
# Decompress data and reconstruct the original XML file
data = bz_decompressor.decompress(compressed_data)
# Write a new XML file with the original data
with open(test_file, 'wb') as f:
    f.write(data)

 
# Uncompressed size is 32,519,723 bytes
# Compressed size is 16,832,446 bytes
# Compression ratio is 0.520821584173746
# Compression efficiency is 1.930474514549746

import pprint
# Create a new data structure
datastructure = dict()
# Iterate over all posts in the 'row' tag and keep track of the number of posts in each 'row'
for event, elem in ET.iterparse(test_file, events=('start', 'end')):
    if event == 'start':
        if elem.tag == 'row':
            datastructure[elem.attrib['Id']] = int(elem.attrib['PostType
