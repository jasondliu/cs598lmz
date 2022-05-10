from lzma import LZMADecompressor
LZMADecompressor.decompress(compressed3)
 
# lzma module throws exception if data is corrupt
# lzma.LZMAError: Input format not supported by decoder
LZMADecompressor.decompress(compressed4)
### Decrypting with Decompressor Objects

# example of 'rot13' cipher
import codecs

def rot13(data):
    return codecs.encode(data, 'rot13')

plain_value = b'This is a test string'
encrypted_value = rot13(plain_value)
encrypted_value

decompressor = codecs.getincrementaldecoder('rot13')()
decompressor.decompress(encrypted_value)
# return bytes in memory
decompressor.flush()
### Handling Incorrect Data

# for example of text encoding
import codecs
try:
    codecs.decode('\xe9', 'cp1252')
except UnicodeDecodeError as err:
    print(err.start)
    print(err.end)
    print(err.reason)
    print(
