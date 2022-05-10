from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("downloads/output.txt.bz2").read()) 

#a = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#print(BZ2Decompressor().decompress(a))

#b'Compress me!'

#b'Compress me!'

#with open("downloads/output.txt", "rb") as data:
#    with BZ2File(data.name, "rb", open("downloads/output.txt.bz2", "rb")) as target:
#        with open("downloads/output_new.txt", "wb") as output:
#            shutil.copyfileobj(target, output)
            
#a = b'BZh91AY&SYA\xaf\x82\r\
