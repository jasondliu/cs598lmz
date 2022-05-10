from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bz2
import bz2
compressed_data = bz2.compress(original_data)
compressed_data

bz2.decompress(compressed_data)

# zlib
import zlib
compressed_data = zlib.compress(original_data)
compressed_data

zlib.decompress(compressed_data)

# pickle
import pickle
pickled_data = pickle.dumps(original_data)
pickled_data

pickle.loads(pickled_data)

# json
import json
json.dumps(original_data)

json.loads(json.dumps(original_data))

# msgpack
import msgpack
msgpack.dumps(original_data)

msgpack.loads(msgpack.dumps(original_data))

# yaml
import yaml
yaml.dump(original_data)

yaml.load(yaml.dump(original_data))

# toml
import to
