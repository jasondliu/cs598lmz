import bz2
bz2.decompress(compressed_data)

print(bz2.decompress(compressed_data))

print(bz2.decompress(compressed_data).decode('utf-8'))

data = b'We are no longer the Knights who say Ni!'
print(len(data))

compressed = bz2.compress(data)
print(len(compressed))

print(bz2.decompress(compressed))

print(bz2.crc32(data))

db = shelve.open('test_shelf.db')
db['cats'] = ['Zophie', 'Pooka', 'Simon']
db.close()

db = shelve.open('test_shelf.db')
print(db['cats'])
db.close()

db = shelve.open('test_shelf.db')
print(db['cats'])
db['cats'].append('Fat-tail')
db['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail']
