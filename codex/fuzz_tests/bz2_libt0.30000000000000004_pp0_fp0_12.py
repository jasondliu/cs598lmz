import bz2
bz2.decompress(compressed_data)

# bz2.decompress(compressed_data)
# TypeError: a bytes-like object is required, not 'str'

# bz2.decompress(compressed_data.encode('utf-8'))
# TypeError: argument 1 must be a bytes-like object, not 'str'

# bz2.decompress(compressed_data.encode('utf-8')).decode('utf-8')
# TypeError: argument 1 must be a bytes-like object, not 'str'

# bz2.decompress(compressed_data.encode('utf-8')).decode('utf-8')
# TypeError: argument 1 must be a bytes-like object, not 'str'

# bz2.decompress(compressed_data.encode('utf-8')).decode('utf-8')
# TypeError: argument 1 must be a bytes-like object, not 'str'

# bz2.decompress(compressed_data.encode('
