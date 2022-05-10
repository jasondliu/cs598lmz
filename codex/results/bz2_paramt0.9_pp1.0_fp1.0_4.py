from bz2 import BZ2Decompressor
BZ2Decompressor().decompress('BZh9\x8a\x00\x00\x01\x00!\x9ah3M\x13<]\xc9\x14\xe1BCe\x00@@')
print

print "Strategy 2: {class-method}"
BZ2Decompressor().decompress(data)
print

print "Strategy 3: {staticmethod-lambda}"
Compressor().decompress(data, 'staticmethod-lambda')
print

print "Strategy 4: {staticmethod}"
Compressor.decompress(data, 'staticmethod')
print

print "Strategy 5: {strategy + class-method}"
Compressor().decompress(data, 'method')
print

print "Strategy 6: {strategy + lambda}"
Compressor().decompress(data, 'lambda')
print

print "Strategy 6c: {strategy + lambda: default behaviour}"
Compressor().decompress(data, 'lambda-default')
print

print "Strategy 7: {strategy + globals}"
Comp
