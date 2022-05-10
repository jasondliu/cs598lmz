import bz2
# Test BZ2Decompressor
with open('../../data/wikipedia/jawiki-country.json.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for line in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
        print(line)

# Test BZ2File
with bz2.BZ2File('../../data/wikipedia/jawiki-country.json.bz2', 'rb') as f:
    for line in f:
        print(line)

# Use BZ2File and json.loads
with bz2.BZ2File('../../data/wikipedia/jawiki-country.json.bz2', 'rb') as f:
    for line in f:
        data_json = json.loads(line)
        print(data_json['title'])

# Read all lines and load them
with bz2.BZ2File('../../data/wikipedia/jawiki-country.json.bz2', 'rb')
