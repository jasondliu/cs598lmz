import bz2
bz2.open('file.bz2')

# bz2.open() function returns a BZ2File object that is a file-like object.
# We can read from or write to it in the same way as a normal file.

# The BZ2File object also has a readline method that we can use to read the
# contents of a file line by line.

# The BZ2File object can also be passed to the json module to decode a JSON
# file.

# The BZ2File object can also be passed to the json module to decode a JSON file.
import json
json_data = bz2.open('file.json.bz2', 'rt')
data = json.load(json_data)
