import bz2
# Test BZ2Decompressor here
input_file = bz2.BZ2File('test.tar.bz2')
decompressor = bz2.BZ2Decompressor()

output = []
while True:
    data = input_file.read(2096)
    if not data:
        break
    
    data = decompressor.decompress(data)
    if not data:
        break
    
    output.append(data)

full_output = b''.join(output)

print(full_output)

## 12. Your HTML chat bot ##

import bz2

# Make your BZ2Decompressor here!
decompressor = bz2.BZ2Decompressor()
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

dec
