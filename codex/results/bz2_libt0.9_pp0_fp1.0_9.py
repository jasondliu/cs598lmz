import bz2
bz2.decompress(with_header).decode('utf-8')

'''
Better error handling

Sometimes compressors get "bad" data that they can't compress, and they want to throw away the data and move on. You can do this by using the errors argument to decode.    

'''


bad_data = bz2.decompress(with_header) + b'foo'

try:
    bad_data.decode('utf-8', errors='strict')
except UnicodeDecodeError as e:
    print(e)
bad_data.decode('utf-8', errors='replace')

# Missing data

bz2.decompress(without_header).decode('utf-8')
bz2.decompress(without_header, wbits=-9).decode('utf-8')


'''
Similarity between bz2 and zlib

The zlib module has a zlib.compress function that behaves structurally like bz2.compress. Likewise, zlib.decompress is structurally similar to bz2.decomp
