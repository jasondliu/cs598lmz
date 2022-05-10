import bz2
# Test BZ2Decompressor
# bz2.BZ2Decompressor()
# bz2.decompress(compressed_intelligence)
# Challenge 1
print(bz2.decompress(compressed_intelligence))

# Challenge 2
print(bz2.decompress(un).decode('utf-8'))

# Challenge 3
import json
print(json.loads(decoded_intelligence.decode('utf-8')))

# Challenge 4
print(d.decode('utf-8'))

# Challenge 5
print(json.loads(bz2.decompress(d).decode('utf-8')))

# Challenge 6
print(json.loads(bz2.decompress(c.decode('utf-8'))))

# Challenge 7
print(json.loads(bz2.decompress(c)).decode('utf-8'))

# Challenge 8
print(json.loads(bz2.decompress(c)).decode('utf-8').split('.')[0])

# Challenge 9
print(json.loads
