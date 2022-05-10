import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename)

import zipfile
zipfile.ZipFile(filename)

# 使用with语句来自动关闭文件
with open(filename) as f:
    data = function(f)

# 使用json.dump()和json.load()
# 写入json
import json
with open(filename, 'w') as f:
    json.dump(data, f)
# 读取json
with open(filename, 'r') as f:
    data = json.load(f)

# 字符串匹配和搜索
text = 'yeah, but no, but yeah, but no, but yeah'
text.find('no')

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
if re.match(r'\d+/\d+/\d+
