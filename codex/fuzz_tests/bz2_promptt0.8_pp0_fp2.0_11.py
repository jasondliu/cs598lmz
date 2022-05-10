import bz2
# Test BZ2Decompressor

print(len(text))
# write the compressed data to a file
with bz2.open('text.bz2', 'wt') as f:
    f.write(text)
# read the compressed data from the file
with bz2.open('text.bz2', 'rt') as f:
    text_from_file = f.read()

print(len(text_from_file))
print(text_from_file)
print(len(bz2.compress(text.encode('utf-8'))))
print(len(bz2.compress(text_from_file.encode('utf-8'))))
 
# 完全一致
print(text == text_from_file)
# 这个例子中，我们可以看到，解压后的长度比解压前的长度长。这是因为，我们
