import lzma
lzma_file_name = 'test_data_lzma.txt.xz'
with lzma.open(lzma_file_name, 'wb') as f:
    f.write(file_content)
!ls -lah {lzma_file_name}

with lzma.open(lzma_file_name, 'rb') as f:
    lzma_file_content = f.read()

print(lzma_file_content)
print(type(lzma_file_content))

print(lzma_file_content.decode('utf-8'))
print(type(lzma_file_content.decode('utf-8')))

lzma.open(lzma_file_name, 'rb').read().decode('utf-8')
 
with open(source_file_name, 'rb') as f:
    file_content = f.read()
    print(compress(file_content, 9))
    
with open('test_data_lzma.txt.x
