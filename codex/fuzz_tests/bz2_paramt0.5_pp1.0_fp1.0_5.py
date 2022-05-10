from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# print(bz2.decompress(bz2_data))

# bz2_file = open('bz2_file.bz2', 'rb')
# print(bz2.decompress(bz2_file.read()))
# bz2_file.close()

# import zipfile
# zip_file = zipfile.ZipFile('zip_file.zip', 'w')
# zip_file.write('bz2_file.bz2')
# zip_file.close()

# import zipfile
# zip_file = zipfile.ZipFile('zip_file.zip')
# print(zip
