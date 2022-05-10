import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress(b'BZh91AY&SY\xc4\x8d\xa8\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
d.decompress(b'\x7f\x00\x00\x00\x01')
# b'BZh91AY&SY\x19\x80P\x81\x11\x00\x00\x00\x07\x00')

# Test MultipartDecoder
md = MultipartDecoder(b'--AaB03x\r\nContent-Disposition: form-data; name="submit-name"\r\n\r\nLarry\r\n--AaB03x\r\nContent-Disposition: form-data; name="files"; filename="file1.txt"\r\nContent-Type: text/
