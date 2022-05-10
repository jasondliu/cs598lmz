from lzma import LZMADecompressor
LZMADecompressor().decompress(file_LZMA)

#Zip
zipped_file = ZipFile('zipped_file.zip', 'w')
zipped_file.write('text.txt')
zipped_file.write('text2.txt')
zipped_file.close

#Unzip
unzipped_file = ZipFile('zipped_file.zip', 'r')
unzipped_file.extractall('unzipped_file')
unzipped_file.close

#Tar
tar = TarFile('tar_file.tar', 'w')
for name in ['text.txt', 'text2.txt']:
    tar.add(name)
tar.close

#UnTar
untar = TarFile('tar_file.tar', 'r')
untar.extractall('untarred_file')
untar.close

#BZ2
with BZ2File('text.bz2', 'w') as compressed:
    text = 'a' * 1000000
    compressed.write(text)

#UnBZ2
with B
