from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# bz2
import bz2
bz2.decompress(data)

# zip
from zipfile import ZipFile
from io import BytesIO
[x.filename for x in ZipFile(BytesIO(data)).infolist()]

'''

# 读写数据

'''
import csv
with open('./data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))

with open('./data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

'''

# 正则表达式

'''
# 检测正则表达式匹配
import
