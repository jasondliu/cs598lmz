import lzma
lzma.decompress(open('xz-compressed', 'rb').read())

# use rarfile module to extract rar files
import rarfile
rar_file = rarfile.RarFile('rar-compressed')
rar_file.extractall()

# use zipfile module to extract zip files
import zipfile
zip_file = zipfile.ZipFile('zip-compressed')
zip_file.extractall()
