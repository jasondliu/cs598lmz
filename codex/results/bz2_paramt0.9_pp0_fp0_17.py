from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(file1comp)

#From file
out = BZ2File('output_comp.bz2', 'wb')
out.write(file1comp)
out.close()
out = BZ2File('output_comp.bz2', 'rb')
print (out.read())

'''




b = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
print ("Original data:", b)

#inbuilt method
print (bz2.decompress(b))

#user defined
decomp = BZ2Decompressor()
decomp.decompress(b)


bz2_file1 = BZ2File("output.bz2", "wb")
bz2_file1.write("Hello World")
bz
