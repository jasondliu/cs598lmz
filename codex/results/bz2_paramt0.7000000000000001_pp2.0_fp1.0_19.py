from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_json)

# Then do it again
compressed_json = bz2.compress(json.dumps(compressed_json).encode('utf-8')).decode('utf-8')
compressed_json

# Use json.loads on the result
json.loads(compressed_json)

# Use json.loads on the result
json.loads(compressed_json)

# Decode the compressed string
decompressed_json = bz2.decompress(compressed_json.encode('utf-8'))

# Decode the compressed string
decompressed_json = bz2.decompress(compressed_json.encode('utf-8'))

# Load the json
json.loads(decompressed_json)
