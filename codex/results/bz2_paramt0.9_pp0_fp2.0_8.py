from bz2 import BZ2Decompressor
BZ2Decompressor

byte_string = bytes('This is a byte string!', 'UTF-8')
byte_string

byte_string[0]

print(byte_string[0])

byte_string[-1]

len(byte_string)

for char in byte_string:
    print(char)
    
    
    
    
if 'i' in byte_string:
    print("could find i")
    
    
    
    
    
    
    
)if not 'p' in byte_string:
    print("couldn't find p")
    
    

data = bytes.fromhex('deadbeef')
data

encoded = data.hex()
encoded

byte_string.decode('UTF-8')

encoded = byte_string.decode('UTF-8')
encoded

print(encoded)

list(byte_string)

_ = b'\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0
