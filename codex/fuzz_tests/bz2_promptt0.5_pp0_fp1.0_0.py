import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('/home/ubuntu/data/test_image.bz2', 'rb') as f_in, open('/home/ubuntu/data/test_image.jpg', 'wb') as f_out:
    for data in iter(lambda : f_in.read(100 * 1024), b''):
        f_out.write(bz2_decompressor.decompress(data))
 
# Test BZ2File

with bz2.BZ2File('/home/ubuntu/data/test_image.bz2', 'rb') as src, open('/home/ubuntu/data/test_image.jpg', 'wb') as dst:
    dst.write(src.read())
 
# Test BZ2File readline()

with bz2.BZ2File('/home/ubuntu/data/test_image.bz2', 'rb') as src, open('/home/ubuntu/data/test_image.jpg', 'wb') as dst:

