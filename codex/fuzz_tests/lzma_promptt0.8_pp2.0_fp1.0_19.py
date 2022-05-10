import lzma
# Test LZMADecompressor speed
source_path = '/media/piotr/Yandex/DAMP/'
i = 1
while os.path.isfile(source_path + 'DAMP_' + str(i) + '.tar.xz'):
    file_path = source_path + 'DAMP_' + str(i) + '.tar.xz'
    i += 1
    with lzma.open(file_path) as f:
        data = f.read()
    print(i)
print(i)

source_path = '/media/piotr/Yandex/DAMP/'
i = 1
while os.path.isfile(source_path + 'DAMP_' + str(i) + '.tar.xz'):
    file_path = source_path + 'DAMP_' + str(i) + '.tar.xz'
    i += 1
    with open(file_path, 'rb') as f:
        data = f.read()
    print(i)
print(i)

# Create some text files with different sizes

