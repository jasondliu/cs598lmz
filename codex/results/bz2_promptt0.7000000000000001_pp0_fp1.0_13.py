import bz2
# Test BZ2Decompressor class
d = bz2.BZ2Decompressor()
d.decompress(b'BZh91AY&SY\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?\xe7\xff\xe00\x01\x99\xaa\x00\xc0-\x10@')

# Test BZ2File class
input_file = bz2.BZ2File(fileobj=b'BZh91AY&SY\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?\xe7\xff\xe00\x01\x99\xaa\x00\xc0-\x10@')
input_file.read()

output_file = bz2.BZ2File('file_path.bz2', 'wb')
output_file.write(b'random content
