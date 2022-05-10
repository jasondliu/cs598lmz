import bz2
# Test BZ2Decompressor.read()
decompressor = BZ2Decompressor()
input_data = bz2.compress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
print(input_data)
print(type(input_data))
print(input_data.find(b"BZh"), input_data.find(b"BZh")+4)
input_data = input_data[input_data.find(b"BZh")+4:-1]
output_data = decompressor.decompress(input_data)
print(output_data)

# split() allows splits on multiple delimiters
print(re.split('; |, |\*|\n', 'ab;cd,ef*gh\nij'))
'''
print(re.match('super
