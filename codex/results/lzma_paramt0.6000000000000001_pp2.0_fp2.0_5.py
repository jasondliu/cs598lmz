from lzma import LZMADecompressor
LZMADecompressor()

# lzma
# decompress
with lzma.open('file.xz', 'rb') as f:
    file_content = f.read()

# compress
with lzma.open('file.xz', 'wb') as f:
    f.write(b"some data that is to be compressed")

# simplejson
import simplejson as json

# json
# load
with open('people.json', 'r') as f:
    people = json.load(f)

# save
with open('people.json', 'w') as f:
    json.dump(people, f, indent=4)

# json
# dumps
s = json.dumps(people)

# loads
people = json.loads(s)

# json
# dump
json.dump(people, f)

# load
people = json.load(f)

# json
# dump
json.dump(people, f)

# load
people = json.load(f)

# json
# dumps
s = json.dumps(
