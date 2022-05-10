from lzma import LZMADecompressor
LZMADecompressor().decompress(open('../tmx/maps/cave1_level1.tmx.lzma', 'rb').read())

data = open('../tmx/maps/cave1_level1.tmx.lzma', 'rb').read()
decompress = LZMADecompressor()
print(decompress.decompress(data))

#%%
import lzma
import pickle

x = "test"
print(x)

pickled_x = pickle.dumps(x)
print(pickled_x)

unpickled_x = pickle.loads(pickled_x)
print(unpickled_x)

with open('test.lzma', 'wb') as f:
    pickled_x = pickle.dumps(x)
    compressed_x = lzma.compress(pickled_x)
    f.write(compressed_x)

with open('test.lzma', 'rb') as f:
    compressed_x = f.read()
    pickled
