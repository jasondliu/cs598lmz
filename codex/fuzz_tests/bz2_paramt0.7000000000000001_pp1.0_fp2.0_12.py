from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# decompress data
decompressed_data = BZ2Decompressor().decompress(data)

# write decompressed data
output = open('data/decompressed_data.xml', 'wb')
output.write(decompressed_data)
output.close()

# load new file and print the first 1000 characters
file = open('data/decompressed_data.xml', 'r')
print(file.read()[0:1000])

# read the decompressed file using BeautifulSoup
file = open('data/decompressed_data.xml', 'rb')
soup = BeautifulSoup(file, 'xml')

# print soup to verify it's a BeautifulSoup object
print(type(soup))

# create and write doc to json file
with open('data/data.json', 'w') as f:
    f.write(soup.prettify())
