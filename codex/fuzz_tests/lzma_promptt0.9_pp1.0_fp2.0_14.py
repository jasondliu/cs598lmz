import lzma
# Test LZMADecompressor to read this file
lz = lzma.LZMADecompressor()

filename = '../repos/Linux-5.5/init/main.o.xz'
with open(filename, 'rb') as f: # b is important -> binary
  file_content = f.read()

file_content = file_content[65:]
decoder = MyDecompressor()
data = decoder.decode(file_content)
print(data)
print('finished')

# data = lz.decompress(file_content)
# print(data)

# data = file_content
# with lzma.open(filename + '.xz') as decompress_file:
#     print(decompress_file.read())



# data = file_content
# with lzma.open(filename + '.xz') as decompress_file:
#     print(decompress_file.read())
#print(type(file_content))
# i = 0
# print(file_content[i])
# i = i + 1

