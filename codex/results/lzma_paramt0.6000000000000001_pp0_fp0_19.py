from lzma import LZMADecompressor
LZMADecompressor().decompress(b'YWJjZA==') # b'abcd'

# compress
# lzma.compress()



# zip
import zipfile

with zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('test.txt')
    zf.write('test2.txt')

with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.namelist())
    print(zf.getinfo('test.txt'))
    print(zf.getinfo('test.txt').file_size)
    print(zf.getinfo('test.txt').compress_size)
    print(zf.read('test.txt'))



# tarfile
import tarfile

with tarfile.open('test.tar', 'w') as tf:
    tf.add('test.txt')
    tf.add('test2.txt')

with tarfile.open('test.tar', 'r') as
