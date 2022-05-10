import bz2
bz2.decompress(data)

#%% 压缩优化
from StringIO import StringIO
import gzip
inmemory = StringIO()
with gzip.GzipFile(fileobj=inmemory, mode='wb') as f:
    f.write('abc')
inmemory.seek(0)

#%% 解压缩
import gzip
f = gzip.open('tmp.gz', 'r')

#%% 操作csv文件
import csv
with open("file.csv", "rb") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open("file.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)

#操作json文件

#解析json文件
import json
data = json.loads(json_string)

#序列化json文件
json
