import bz2
bz2_file = bz2.BZ2File('douban_comments_20170807.csv.bz2')
for line in bz2_file:
    print(line)
    break

# 遍历csv文件
import csv
csv_file = csv.reader(open('douban_comments_20170807.csv'))
for line in csv_file:
    print(line)
    break

# 遍历txt文件
with open('douban_comments_20170807.txt', 'r', encoding='utf8') as txt_file:
    for line in txt_file:
        print(line)
        break

# 遍历gz压缩文件
import gzip
gz_file = gzip.open('douban_comments_20170807.csv.gz', 'rt')
for line in gz_file:
    print(line)
    break

```

```python
import pandas as pd
df =
