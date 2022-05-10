import bz2
bz2.decompress(data)

import gzip
gzip.decompress(data)

# 文字コード
import codecs
codecs.lookup('utf-8') # ('utf_8', <class 'codecs.utf_8'>, 12)
codecs.lookup('utf_8') # ('utf_8', <class 'codecs.utf_8'>, 12)

import unicodedata
unicodedata.name('あ')
unicodedata.name('あ'.encode('utf-8')) # 'LATIN SMALL LETTER A WITH MACRON'

# ファイル操作
import pathlib
pathlib.Path.cwd()
pathlib.Path.home()

# ファイル操作
import os
os.getcwd()
os.listdir()
os.listdir('.')

os.remove('sample.txt')
os.rmdir('sample.txt')

# ファイル操作
import shutil
sh
