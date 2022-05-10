from bz2 import BZ2Decompressor
BZ2Decompressor()

#generating a new file having bz2compress
with open("test.txt",'w') as file:
    name='shubham vashisht'
    file.write(name)
    file.close()

with BZ2File("test.bz2",'w') as file:
    with open("test.txt",'r') as file1:
        file.write(file1.read().encode("utf-8"))
        file.close()
        file1.close()

with BZ2File("test.bz2",'r') as file:
    file_content=file.read()
    print(file_content.decode("utf-8"))
    file.close()



#lzma
from lzma import LZMACompressor,LZMADecompressor
LZMACompressor()
LZMADecompressor()

#compressing file with the help of lzma
with open("test.txt",'w') as file:
    name='shubham vashisht'
   
