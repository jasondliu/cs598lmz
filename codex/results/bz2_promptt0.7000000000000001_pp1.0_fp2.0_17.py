import bz2
# Test BZ2Decompressor.
from io import BytesIO
from bz2 import BZ2Decompressor

decompressor = BZ2Decompressor()

with open('sample.bz2', 'rb') as input:
    file_content = input.read()
    print(type(file_content))
    print(file_content)
    print(decompressor.decompress(file_content))

with open('sample.bz2', 'rb') as input:
    file_content = input.read()
    print(type(file_content))
    decompressor = BZ2Decompressor()
    print(decompressor.decompress(file_content))
    print(decompressor.unused_data)



# Test BZ2File.
with BZ2File('sample.bz2', 'rb') as input:
    print(input.read())

with BZ2File('sample.bz2', 'rb') as input:
    print(input.peek(10))

with BZ2File('sample.bz2', 'rb
