import bz2
bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084").decode("utf-8")


#Q2. Decompress the bz2 to 'file' folder
#bz2 file is compressed with bz2 library
import bz2
import os
with open('file/file2', 'w') as f2:
	f2.write(bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084").decode("utf-8"))
print(f2)



