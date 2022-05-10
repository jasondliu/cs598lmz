import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
decompressor = bz2.BZ2Decompressor()

try:
    print(decompressor.decompress(data))
    print(decompressor.flush())
except IOError as e:
    print("error:", e)

# Test BZ2File
output = bz2.BZ2File('lorem.txt.bz2', 'wb')
try:
    output.write(data)
finally:
    output.close()

print(bz2.decompress(data))

print("-" * 20)
print("bz2.decompress(bz2.compress(string)) == string:", bz2.decompress(bz2.comp
