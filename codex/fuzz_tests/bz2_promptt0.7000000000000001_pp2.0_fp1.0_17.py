import bz2
# Test BZ2Decompressor

input_file = bz2.BZ2File('/media/jwong/Transcend/VQADataset/Images/train2014/COCO_train2014_000000226799.jpg.bz2')
output_file = open('/home/jwong/Downloads/test.jpg', 'wb')
decompressor = bz2.BZ2Decompressor()

for data in iter(lambda : input_file.read(100 * 1024), b''):
    output_file.write(decompressor.decompress(data))
    
output_file.close()
input_file.close()

# Test BZ2Compressor

input_file = open('/home/jwong/Downloads/test.jpg', 'rb')
output_file = bz2.BZ2File('/home/jwong/Downloads/test.jpg.bz2', 'wb')
compressor = bz2.BZ2Compressor()

while True:
    data = input_file.read(1024)
    if not data
