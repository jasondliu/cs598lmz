import bz2
# Test BZ2Decompressor

text = bz2.compress(b"Hello, world!")

decompressor = bz2.BZ2Decompressor()
d_data = decompressor.decompress(text)
print(d_data)
d_data = decompressor.decompress(b'')
print(d_data)

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'')
try: 
    d_data = decompressor.decompress(text)
except:
    print('Error')

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'garbage')
try: 
    d_data = decompressor.decompress(text)
except:
    print('Error')
    
    
decompressor = bz2.BZ2Decompressor()
d_data = decompressor.decompress(text)
try: 
    d_data = decompressor.decompress(text)
except:
    print('Error')
