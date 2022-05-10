import bz2
# Test BZ2Decompressor on some data:
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
# Feed more data, and check the final result:
print(decompressor.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'))
print(decompressor.flush())

#PERSISTENCE

#Pickling

#Using the pickle module, it is trivial to serialize a Python data structure as a byte stream and reload it.
#When you unpickle a data stream, you get back an object that is identical to the original object.
import pickle
#The pickle module can
