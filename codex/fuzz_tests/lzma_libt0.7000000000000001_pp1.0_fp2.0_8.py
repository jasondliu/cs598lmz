import lzma
lzma.open
'''

'''
import tarfile
tar_file = tarfile.open('./python-3.7.3.tar.xz')
tar_file.extractall(path='./')
'''

'''
import zipfile
zip_file = zipfile.ZipFile('./sample.zip')
zip_file.extractall('./')
'''

'''
import rarfile
rar_file = rarfile.RarFile('./sample.rar')
rar_file.extractall('./')
'''

'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--filename', default='sample.txt', help='input file name')
args = parser.parse_args()
with open(args.filename) as f:
    print(f.read())
'''
