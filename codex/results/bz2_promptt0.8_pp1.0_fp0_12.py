import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open(bz2_filename,'rb') as file:
    decompressor.decompress(file.read())

# Test open
with bz2.open(bz2_filename,'rb') as file:
    if file.read() == open(filename,'r').read():
        print('test open success!')

# Check compress
com_data = bz2.compress(raw_data)
if com_data == open(bz2_filename,'rb').read():
    print('compress two ways match')

# Compress method 1
with open(bz2_filename,'rb') as file:
    if bz2.decompress(file.read()) == raw_data:
        print('decopress matched')

# Compress method 2
with open(bz2_filename,'rb') as file, open(filename,'wb') as out_file:
    decompressor = bz2.BZ2Decompressor()
    while True:
        chunk = file.read(100
