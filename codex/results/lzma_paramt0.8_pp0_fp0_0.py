from lzma import LZMADecompressor
LZMADecompressor.__module__

import shutil
import os

# class ZipVar(object):
#     def __init__(self):
#         self.archive = None
#         self.

if not os.path.exists('/tmp/example'):
    os.makedirs('/tmp/example')

# archive = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)
# for root, dirs, files in os.walk('/tmp/example'):
#     for file in files:
#         archive.write(os.path.join(root, file), arcname=os.path.join(os.path.basename(root), file))
# archive.close()

# archive = zipfile.ZipFile('test.zip', 'r')
# for file in archive.infolist():
#     print(file)
#     print(file.filename)
# archive.extractall('/tmp/example2')
# archive.close()
#
#
# shutil.rmtree('/tmp/example2
