import bz2
bz2.compress()

import zlib
zlib.compress()

import zipfile
zipfile.ZipFile()

import shutil
shutil.copyfile()
shutil.copy()
shutil.copytree()

# 对比文件
import filecmp
filecmp.cmp()
filecmp.dircmp()
"""

"""
import os

print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('../', 'testdir'))
#
