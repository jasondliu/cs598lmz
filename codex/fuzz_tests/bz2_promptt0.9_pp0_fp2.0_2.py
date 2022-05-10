import bz2
# Test BZ2Decompressor
inputfile = bz2.BZ2File('input.json.bz2', 'rb')
config = json.loads(inputfile.read().decode('utf-8'))
print(config)
# convert the config dict to json format
outputfile = bz2.BZ2File('output.json.bz2', 'wb')
outputfile.write(json.dumps(config).encode('utf-8'))
# compress string
uncompressed = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*10
compressed = bz2.compress(uncompressed)
len(compressed)

#Decompress data
uncompressed2 = bz2.decompress(compressed)
print(uncompressed==uncompressed2)
print(uncompressed2)

# compress data streams
compressor = bz2.BZ2Compressor()
compressed2 = compressor.compress(uncompressed)
compressed2 += compressor.flush()
len(compressed2)

#decompress data streams

