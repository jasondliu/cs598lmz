from bz2 import BZ2Decompressor
BZ2Decompressor()

#generating a new file having bz2compress
with open("test.txt",'w') as file:
    name='shubham vashisht'
    file.write(name)
    file.close()

